from sqlmodel import Field, Relationship

from services._shared.domain.entities.policy import Policy
from .bases.entity_base import EntityBase

class PolicyCSP(EntityBase, table=True):
    policy_csp_id: str = Field(primary_key=True)
    policy_id: str = Field(foreign_key="policy.policy_id")
    cloud_type: str = Field(foreign_key="csp.cloud_type")

    policy: "Policy" = Relationship(back_populates="policy_csps")
    csp: "CSP" = Relationship(back_populates="policies")