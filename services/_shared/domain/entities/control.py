
from sqlmodel import Field, Relationship

from services._shared.domain.entities.compliance_standard import ComplianceStandard
from services._shared.domain.entities.control_section import ControlSection
from .bases.entity_base import EntityBase
from typing import Optional

class Control(EntityBase, table=True):
    control_id: str = Field(primary_key=True)
    standard_id: str = Field(foreign_key="compliancestandard.standard_id")
    name: str
    description: Optional[str]
    condition_json: Optional[str]
    remediation: Optional[str]

    standard: "ComplianceStandard" = Relationship(back_populates="controls")
    sections: list["ControlSection"] = Relationship(back_populates="control")