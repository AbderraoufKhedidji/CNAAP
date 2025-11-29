from sqlalchemy.orm import relationship
from _shared.domain.entities.bases.column_types import IdColumn, StringCol
from _shared.domain.entities.bases.entity_base import EntityBase

class ServiceName(EntityBase):
    __tablename__ = "service_names"

    name = StringCol(nullable=False)
    cloud_type = StringCol(nullable=True)

    csps = relationship("CSP", back_populates="services")
    asset_types = relationship("AssetType", back_populates="services")
