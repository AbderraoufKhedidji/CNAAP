from sqlalchemy.orm import relationship
from _shared.domain.entities.bases.column_types import ForeignIdColumn, IdColumn, StringCol
from _shared.domain.entities.bases.entity_base import EntityBase

class AssetType(EntityBase):
    __tablename__ = "asset_types"

    name = StringCol(nullable=False)
    service_name_id = ForeignIdColumn(foreign_key="service_names.id", nullable=False)

    services = relationship("ServiceName", back_populates="asset_types")
    assets = relationship("AssetName", back_populates="asset_types")
