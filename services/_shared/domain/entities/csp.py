from typing import Optional
from sqlmodel import Field, Relationship
from services._shared.domain.entities.policy_csp import PolicyCSP
from services._shared.domain.entities.service_name import ServiceName
from .bases.entity_base import EntityBase


class CSP(EntityBase, table=True):
    cloud_type: str = Field(primary_key=True)
    resource_name: Optional[str]
    total_pass_policies: Optional[int]
    total_failed_policies: Optional[int]

    policies: list["PolicyCSP"] = Relationship(back_populates="csp")
    services: list["ServiceName"] = Relationship(back_populates="csp")