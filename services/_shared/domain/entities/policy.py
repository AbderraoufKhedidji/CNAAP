import uuid
from sqlmodel import Field, Relationship
from services._shared.domain.entities.policy_csp import PolicyCSP
from services._shared.domain.entities.section_policy import SectionPolicy
from .bases.entity_base import EntityBase
from typing import Optional


class Policy(EntityBase, table=True):
    id: str = Field(primary_key=True)
    name: str
    description: Optional[str]
    policy_type: Optional[str]
    cloud_type: Optional[str]
    severity: Optional[str]
    enabled: Optional[bool]
    compliance_requirement: Optional[str]

    section_policies: list["SectionPolicy"] = Relationship(back_populates="policy")
    policy_csps: list["PolicyCSP"] = Relationship(back_populates="policy")
    alerts: list["Alerts"] = Relationship(back_populates="policy")
