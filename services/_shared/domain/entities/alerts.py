import datetime
from typing import Optional
from sqlmodel import Field, Relationship
from services._shared.domain.entities.event_alert import EventAlert
from services._shared.domain.entities.service_name import ServiceName
from .bases.entity_base import EntityBase

class Alerts(EntityBase, table=True):
    alert_id: str = Field(primary_key=True)
    alert_name: str
    status: Optional[bytes]
    resolved_on: Optional[datetime]
    resolution_reason: Optional[str]
    policy_id: str = Field(foreign_key="policy.policy_id")
    vpc_name: Optional[str]
    tags: Optional[str]

    policy: "Policy" = Relationship(back_populates="alerts")
    event_alerts: list["EventAlert"] = Relationship(back_populates="alert")