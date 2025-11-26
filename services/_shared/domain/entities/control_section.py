
from sqlmodel import Field, Relationship

from services._shared.domain.entities.control import Control
from services._shared.domain.entities.section_policy import SectionPolicy
from .bases.entity_base import EntityBase
from typing import Optional

class ControlSection(EntityBase, table=True):
    section_id: str = Field(primary_key=True)
    control_id: str = Field(foreign_key="control.control_id")
    name: str
    description: Optional[str]
    order_number: Optional[int]

    control: "Control" = Relationship(back_populates="sections")
    section_policies: list["SectionPolicy"] = Relationship(back_populates="section")