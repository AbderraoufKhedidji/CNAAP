from sqlalchemy.orm import relationship
from _shared.domain.entities.bases.column_types import ForeignIdColumn, IdColumn, StringCol
from _shared.domain.entities.bases.entity_base import EntityBase

class PolicyCSP(EntityBase):
    __tablename__ = "policy_csp"

    policy_id = IdColumn(primary_key=False)
    cloud_type = ForeignIdColumn(foreign_key="csp.cloud_type", nullable=False)

    policies = relationship("Policy", back_populates="policy_csps")
    csps = relationship("CSP", back_populates="policies")
