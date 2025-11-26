from sqlmodel import Field, Relationship
from services._shared.domain.entities.service_name import ServiceName
from .bases.entity_base import EntityBase

class AssetType(EntityBase, table=True):
    asset_type_id: str = Field(primary_key=True)
    asset_type: str
    service_name_id: str = Field(foreign_key="servicename.service_name_id")

    service: "ServiceName" = Relationship(back_populates="asset_types")
    asset_names: list["AssetName"] = Relationship(back_populates="asset_type")