from typing import Optional
from sqlmodel import Field, Relationship
from services._shared.domain.entities.asset_type import AssetType
from services._shared.domain.entities.event import Event
from .bases.entity_base import EntityBase


class EventAlert(EntityBase, table=True):
    event_alert_id: str = Field(primary_key=True)
    alert_id: str = Field(foreign_key="alerts.alert_id")
    event_id: str = Field(foreign_key="event.event_id")

    alert: "Alerts" = Relationship(back_populates="event_alerts")
    event: "Event" = Relationship(back_populates="event_alerts")