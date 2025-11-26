from sqlmodel import Field, Relationship

from services._shared.domain.entities.control_section import ControlSection
from services._shared.domain.entities.policy import Policy
from .bases.entity_base import EntityBase

class SectionPolicy(EntityBase, table=True):
    section_policy_id: str = Field(primary_key=True)
    section_id: str = Field(foreign_key="controlsection.section_id")
    policy_id: str = Field(foreign_key="policy.policy_id")

    section: "ControlSection" = Relationship(back_populates="section_policies")
    policy: "Policy" = Relationship(back_populates="section_policies")