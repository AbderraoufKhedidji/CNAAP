from sqlalchemy.orm import relationship
from _shared.domain.entities.bases.column_types import ForeignIdColumn, IdColumn, StringCol
from _shared.domain.entities.bases.entity_base import EntityBase

class Control(EntityBase):
    __tablename__ = "controls"

    standard_id = ForeignIdColumn(foreign_key="compliance_standard.id")
    name = StringCol(nullable=False)
    description = StringCol(nullable=True)
    condition_json = StringCol(nullable=True)
    remediation = StringCol(nullable=True)

    standard = relationship("ComplianceStandard", back_populates="controls")
    sections = relationship("ControlSection", back_populates="controls")
