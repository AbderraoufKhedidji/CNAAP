from typing import Optional
from sqlmodel import Field, Relationship
from services._shared.domain.entities.asset_type import AssetType
from .bases.entity_base import EntityBase

class AssetName(EntityBase, table=True):
    asset_name_id: str = Field(primary_key=True)
    asset_name: str
    asset_type_id: str = Field(foreign_key="assettype.asset_type_id")
    account_id: Optional[str]
    account_name: Optional[str]
    asset_id: Optional[str]
    region_id: Optional[str]
    region: Optional[str]

    asset_type: "AssetType" = Relationship(back_populates="asset_names")
    events: list["Event"] = Relationship(back_populates="asset_name")