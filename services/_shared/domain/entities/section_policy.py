from sqlalchemy.orm import relationship
from _shared.domain.entities.bases.column_types import ForeignIdColumn, IdColumn
from _shared.domain.entities.bases.entity_base import EntityBase

class SectionPolicy(EntityBase):
    __tablename__ = "section_policy"

    #section_id = ForeignIdColumn("sections.id")
    policy_id = ForeignIdColumn("policies.id")

    #section = relationship("ControlSection", back_populates="section_policies")
    policy = relationship("Policy", back_populates="section_policies")
