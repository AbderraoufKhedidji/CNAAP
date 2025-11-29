from sqlalchemy.orm import relationship
from _shared.domain.entities.bases.column_types import IntegerCol, StringCol
from _shared.domain.entities.bases.entity_base import EntityBase

class CSP(EntityBase):
    __tablename__ = "csp"

    cloud_type = StringCol(primary_key=True)
    resource_name = StringCol(nullable=True)
    total_pass_policies = IntegerCol(nullable=True)
    total_failed_policies = IntegerCol(nullable=True)

    policies = relationship("PolicyCSP", back_populates="csps")
    services = relationship("ServiceName", back_populates="csps")
