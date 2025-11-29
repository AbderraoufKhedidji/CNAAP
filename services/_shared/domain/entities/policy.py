from sqlalchemy.orm import relationship
from _shared.domain.entities.bases.column_types import IdColumn, StringCol, BoolCol
from _shared.domain.entities.bases.entity_base import EntityBase

class Policy(EntityBase):
    __tablename__ = "policies"

    name = StringCol(nullable=False)
    description = StringCol(nullable=True)
    policy_type = StringCol(nullable=True)
    cloud_type = StringCol(nullable=True)
    severity = StringCol(nullable=True)
    enabled = BoolCol(nullable=True)
    compliance_requirement = StringCol(nullable=True)

    section_policies = relationship("SectionPolicy", back_populates="policies")
    policy_csps = relationship("PolicyCSP", back_populates="policies")
    alerts = relationship("Alert", back_populates="policies")
