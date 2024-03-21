# automatically generated by the FlatBuffers compiler, do not modify

# namespace: hcf

import flatbuffers
from flatbuffers.compat import import_numpy
from typing import Any
from hushh.hcf.ProductVibes import ProductVibes
from typing import Optional
np = import_numpy()

class Catalog(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset: int = 0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Catalog()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsCatalog(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # Catalog
    def Init(self, buf: bytes, pos: int):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Catalog
    def Id(self) -> Optional[str]:
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Catalog
    def Version(self) -> Optional[str]:
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Catalog
    def Description(self) -> Optional[str]:
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Catalog
    def ProductVibes(self) -> Optional[ProductVibes]:
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            obj = ProductVibes()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Catalog
    def BatchSize(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # Catalog
    def TokenizerNameOrPath(self) -> Optional[str]:
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Catalog
    def ModelNameOrPath(self) -> Optional[str]:
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def CatalogStart(builder: flatbuffers.Builder):
    builder.StartObject(7)

def Start(builder: flatbuffers.Builder):
    CatalogStart(builder)

def CatalogAddId(builder: flatbuffers.Builder, id: int):
    builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(id), 0)

def AddId(builder: flatbuffers.Builder, id: int):
    CatalogAddId(builder, id)

def CatalogAddVersion(builder: flatbuffers.Builder, version: int):
    builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(version), 0)

def AddVersion(builder: flatbuffers.Builder, version: int):
    CatalogAddVersion(builder, version)

def CatalogAddDescription(builder: flatbuffers.Builder, description: int):
    builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(description), 0)

def AddDescription(builder: flatbuffers.Builder, description: int):
    CatalogAddDescription(builder, description)

def CatalogAddProductVibes(builder: flatbuffers.Builder, productVibes: int):
    builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(productVibes), 0)

def AddProductVibes(builder: flatbuffers.Builder, productVibes: int):
    CatalogAddProductVibes(builder, productVibes)

def CatalogAddBatchSize(builder: flatbuffers.Builder, batchSize: int):
    builder.PrependInt32Slot(4, batchSize, 0)

def AddBatchSize(builder: flatbuffers.Builder, batchSize: int):
    CatalogAddBatchSize(builder, batchSize)

def CatalogAddTokenizerNameOrPath(builder: flatbuffers.Builder, tokenizerNameOrPath: int):
    builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(tokenizerNameOrPath), 0)

def AddTokenizerNameOrPath(builder: flatbuffers.Builder, tokenizerNameOrPath: int):
    CatalogAddTokenizerNameOrPath(builder, tokenizerNameOrPath)

def CatalogAddModelNameOrPath(builder: flatbuffers.Builder, modelNameOrPath: int):
    builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(modelNameOrPath), 0)

def AddModelNameOrPath(builder: flatbuffers.Builder, modelNameOrPath: int):
    CatalogAddModelNameOrPath(builder, modelNameOrPath)

def CatalogEnd(builder: flatbuffers.Builder) -> int:
    return builder.EndObject()

def End(builder: flatbuffers.Builder) -> int:
    return CatalogEnd(builder)

import hushh.hcf.ProductVibes
try:
    from typing import Optional
except:
    pass

class CatalogT(object):

    # CatalogT
    def __init__(self):
        self.id = None  # type: str
        self.version = None  # type: str
        self.description = None  # type: str
        self.productVibes = None  # type: Optional[hushh.hcf.ProductVibes.ProductVibesT]
        self.batchSize = 0  # type: int
        self.tokenizerNameOrPath = None  # type: str
        self.modelNameOrPath = None  # type: str

    @classmethod
    def InitFromBuf(cls, buf, pos):
        catalog = Catalog()
        catalog.Init(buf, pos)
        return cls.InitFromObj(catalog)

    @classmethod
    def InitFromPackedBuf(cls, buf, pos=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, pos)
        return cls.InitFromBuf(buf, pos+n)

    @classmethod
    def InitFromObj(cls, catalog):
        x = CatalogT()
        x._UnPack(catalog)
        return x

    # CatalogT
    def _UnPack(self, catalog):
        if catalog is None:
            return
        self.id = catalog.Id()
        self.version = catalog.Version()
        self.description = catalog.Description()
        if catalog.ProductVibes() is not None:
            self.productVibes = hushh.hcf.ProductVibes.ProductVibesT.InitFromObj(catalog.ProductVibes())
        self.batchSize = catalog.BatchSize()
        self.tokenizerNameOrPath = catalog.TokenizerNameOrPath()
        self.modelNameOrPath = catalog.ModelNameOrPath()

    # CatalogT
    def Pack(self, builder):
        if self.id is not None:
            id = builder.CreateString(self.id)
        if self.version is not None:
            version = builder.CreateString(self.version)
        if self.description is not None:
            description = builder.CreateString(self.description)
        if self.productVibes is not None:
            productVibes = self.productVibes.Pack(builder)
        if self.tokenizerNameOrPath is not None:
            tokenizerNameOrPath = builder.CreateString(self.tokenizerNameOrPath)
        if self.modelNameOrPath is not None:
            modelNameOrPath = builder.CreateString(self.modelNameOrPath)
        CatalogStart(builder)
        if self.id is not None:
            CatalogAddId(builder, id)
        if self.version is not None:
            CatalogAddVersion(builder, version)
        if self.description is not None:
            CatalogAddDescription(builder, description)
        if self.productVibes is not None:
            CatalogAddProductVibes(builder, productVibes)
        CatalogAddBatchSize(builder, self.batchSize)
        if self.tokenizerNameOrPath is not None:
            CatalogAddTokenizerNameOrPath(builder, tokenizerNameOrPath)
        if self.modelNameOrPath is not None:
            CatalogAddModelNameOrPath(builder, modelNameOrPath)
        catalog = CatalogEnd(builder)
        return catalog
