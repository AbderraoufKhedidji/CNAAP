from sqlmodel import Field, Relationship
from services._shared.domain.entities.asset_type import AssetType
from services._shared.domain.entities.csp import CSP
from .bases.entity_base import EntityBase

class ServiceName(EntityBase, table=True):
    service_name_id: str = Field(primary_key=True)
    service_name: str
    cloud_type: str = Field(foreign_key="csp.cloud_type")

    csp: "CSP" = Relationship(back_populates="services")
    asset_types: list["AssetType"] = Relationship(back_populates="service")