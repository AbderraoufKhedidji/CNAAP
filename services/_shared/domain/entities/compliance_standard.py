
from sqlmodel import Field, Relationship

from services._shared.domain.entities.control import Control
from .bases.entity_base import EntityBase
from typing import Optional

class ComplianceStandard(EntityBase, table=True):
    standard_id: str = Field(primary_key=True)
    name: str
    description: Optional[str]
    cloud_type: Optional[str]

    controls: list["Control"] = Relationship(back_populates="standard")