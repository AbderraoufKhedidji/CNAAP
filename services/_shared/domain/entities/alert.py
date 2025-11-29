from sqlalchemy.orm import relationship
from _shared.domain.entities.bases.column_types import ForeignIdColumn, IdColumn, StringCol, BoolCol, DateTimeCol
from _shared.domain.entities.bases.entity_base import EntityBase

class Alert(EntityBase):
    __tablename__ = "alerts"

    name = StringCol(nullable=False)
    status = BoolCol(default=True, nullable=True)
    resolved_on = DateTimeCol(nullable=True)
    resolution_reason = StringCol(nullable=True)
    policy_id = ForeignIdColumn(foreign_key="policies.id", nullable=False)
    vpc_name = StringCol(nullable=True)
    tags = StringCol(nullable=True)

    policies = relationship("Policy", back_populates="alerts")
    event_alerts = relationship("EventAlert", back_populates="alerts")
