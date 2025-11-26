
import datetime
import time
from typing import Optional
from sqlmodel import Field, Relationship
from services._shared.domain.entities.asset_name import AssetName
from .bases.entity_base import EntityBase


class Event(EntityBase, table=True):
    event_id: str = Field(primary_key=True)
    asset_id: Optional[str]
    event_time: datetime
    account_id: Optional[str]
    account: Optional[str]
    region: Optional[str]
    snoozed_for: Optional[str]
    snoozed_expired: Optional[time]
    reason: Optional[str]
    account_owners: Optional[str]
    asset_name_id: str = Field(foreign_key="assetname.asset_name_id")

    asset_name: "AssetName" = Relationship(back_populates="events")
    event_alerts: list["EventAlert"] = Relationship(back_populates="event")