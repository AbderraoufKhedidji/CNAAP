from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from _shared.domain.entities.bases.column_types import IdColumn
from _shared.domain.entities.bases.entity_base import EntityBase

class EventAlert(EntityBase):
    __tablename__ = "event_alert"

    alert_id = IdColumn()
    event_id = IdColumn()

    alerts = relationship("Alert", back_populates="event_alerts")
    events = relationship("Event", back_populates="event_alerts")
