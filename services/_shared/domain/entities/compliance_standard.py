from sqlalchemy.orm import relationship
from _shared.domain.entities.bases.column_types import IdColumn, StringCol
from _shared.domain.entities.bases.entity_base import EntityBase

class ComplianceStandard(EntityBase):
    __tablename__ = "compliance_standard"

    name = StringCol(nullable=False)
    description = StringCol(nullable=True)
    cloud_type = StringCol(nullable=True)

    controls = relationship("Control", back_populates="standard")
