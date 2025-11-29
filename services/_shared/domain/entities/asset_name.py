from sqlalchemy.orm import relationship
from _shared.domain.entities.bases.column_types import ForeignIdColumn, IdColumn, StringCol
from _shared.domain.entities.bases.entity_base import EntityBase

class AssetName(EntityBase):
    __tablename__ = "asset_names"

    name = StringCol(nullable=False)
    asset_type_id = ForeignIdColumn(foreign_key="asset_types.id", nullable=False)
    account_id = StringCol(nullable=True)
    account_name = StringCol(nullable=True)
    asset_id = StringCol(nullable=True)
    region_id = StringCol(nullable=True)
    region = StringCol(nullable=True)

    asset_types = relationship("AssetType", back_populates="assets")
    events = relationship("Event", back_populates="assets")
