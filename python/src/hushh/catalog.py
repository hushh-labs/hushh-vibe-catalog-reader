import base64
import uuid
from io import BytesIO
from typing import Callable, Dict, List, Optional, Union

from PIL import Image
from PIL.Image import Image as ImageT
from transformers import CLIPModel, ProcessorMixin

from hushh.hcf.Catalog import CatalogT
from hushh.hcf.Category import CategoryT
from hushh.hcf.FlatEmbeddingBatch import FlatEmbeddingBatchT
from hushh.hcf.Product import ProductT
from hushh.hcf.ProductVibes import ProductVibesT
from hushh.hcf.Vibe import VibeT
from hushh.hcf.VibeMode import VibeMode

from .version import VERSION

Processor = Union[ProcessorMixin, Callable]


class IdBase:
    id: str
    base = ""

    def genId(self):
        return self.base + "-" + str(uuid.uuid1())


class Product(ProductT, IdBase):
    def __init__(self, description: str, url: str, image: ImageT | str, imageUrl: str):
        self.id = self.genId()
        self.description = description
        self.url = url
        if isinstance(image, ImageT):
            buffered = BytesIO()
            image.save(buffered, format="JPEG")
            img_str = base64.b64encode(buffered.getvalue())
            self.base64 = img_str.decode("utf-8")
        else:
            self.base64 = image

        self.imageUrl = imageUrl
        self.textVibes = []
        self.imageVibes = []


class VibeBase(IdBase):
    _products: Dict[str, int] = {}

    def addProduct(self, p: Product | str):
        if isinstance(p, str):
            self._products[p] = True
        else:
            self._products[p.id] = True


class Category(CategoryT, VibeBase):
    def __init__(self, description: str, url: str):
        self.base = "CTG"
        self.id = self.genId()
        self.description = description
        self.url = url
        self.productIx = []


class Vibe(VibeT, VibeBase):
    def __init__(self, image: ImageT | str, description: str):
        self.base = "IVB"
        self.id = self.genId()
        self.description = description
        if isinstance(image, ImageT):
            buffered = BytesIO()
            image.save(buffered, format="JPEG")
            img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
            self.base64 = img_str
        else:
            self.base64 = image

        # self.base64 = base64 if base64 is not None else ""
        self.productIdx = []


class FlatEmbeddingBatch(FlatEmbeddingBatchT, IdBase):
    def __init__(self, dim: int, type: int, flatTensor: Optional[List[float]] = None):
        self.base = "FEB"
        self.id = self.genId()
        self.dim = dim
        self.type = type
        self.flatTensor = flatTensor if flatTensor is not None else []


class ProductVibes(ProductVibesT, VibeBase):
    def __init__(self):
        self.base = "PVB"
        self.id = self.genId()
        self.products = []

        self.categories = []
        self._categories = {}

        self.vibes = []
        self._vibes = {}

        self.flatBatches = []


class Catalog(CatalogT, IdBase):
    productVibes: ProductVibes

    def __init__(self, description: str, processor: Processor):
        self.base = "CLG"
        self.id = self.genId()
        self.version = VERSION
        self.description = description
        self.processor = processor
        self.productVibes = ProductVibes()

    def renderProductFlatBatch(self):
        images = []
        texts = []

        model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")

        for p in self.productVibes.products:
            image = Image.open(BytesIO(base64.b64decode(p.base64)))
            images.append(image)
            text = p.description
            texts.append(text)

        inputs = self.processor(
            text=texts,
            images=images,
            return_tensors="pt",
            padding=True,
        )

        image_features = model.get_image_features(
            pixel_values=inputs.pixel_values,
        )

        embedding_dim = image_features.shape[1]
        image_batch = FlatEmbeddingBatch(
            dim=embedding_dim,
            flatTensor=image_features.flatten().tolist(),
            type=VibeMode.ProductImage,
        )
        self.productVibes.flatBatches.append(image_batch)

        text_features = model.get_text_features(
            input_ids=inputs.input_ids,
        )
        embedding_dim = text_features.shape[1]
        text_batch = FlatEmbeddingBatch(
            dim=embedding_dim,
            flatTensor=text_features.flatten().tolist(),
            type=VibeMode.ProductText,
        )
        self.productVibes.flatBatches.append(text_batch)

    def Pack(self, builder):
        self.renderProductFlatBatch()
        super().Pack(builder)

    def addProduct(self, p: Product):
        if p.id in self.productVibes._products:
            raise ValueError(f"Product {p.id} already exists")
        self.productVibes._products[p.id] = len(self.productVibes.products)
        self.productVibes.products.append(p)

    def addProductCategory(self, c: Category):
        if c.id in self.productVibes._categories:
            raise ValueError(f"Category {c.id} already exists")
        self.productVibes._categories[c.id] = len(self.productVibes.categories)
        self.productVibes.categories.append(c)

    def addProductVibe(self, v: Vibe):
        if v.id in self.productVibes._vibes:
            raise ValueError(f"Vibe {v.id} already exists")
        self.productVibes._vibes[v.id] = len(self.productVibes.vibes)
        self.productVibes.vibes.append(v)

    def linkProductCategory(self, p_id: str, c_id: str):
        if p_id not in self.productVibes._products:
            raise ValueError(f"Product {p_id} does not exist in Catalog")
        if c_id not in self.productVibes._categories:
            raise ValueError(f"Category {c_id} does not exist in Catalog")

        c_idx = self.productVibes._categories[c_id]
        p_idx = self.productVibes._products[p_id]
        self.productVibes.categories[c_idx].productIdx.append(p_idx)

    def linkProductVibe(self, p_id: str, v_id: str):
        if v_id not in self.productVibes._vibes:
            raise ValueError(f"Vibe {v_id} does not exist in Catalog")

        p_idx = self.productVibes._products[p_id]
        v_idx = self.productVibes._vibes[v_id]
        self.productVibes.vibes[v_idx].productIdx.append(p_idx)
