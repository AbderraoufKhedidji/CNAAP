from sqlalchemy.orm import relationship
from _shared.domain.entities.bases.column_types import ForeignIdColumn, IdColumn, IntegerCol, StringCol
from _shared.domain.entities.bases.entity_base import EntityBase

class ControlSection(EntityBase):
    __tablename__ = "control_section"

    control_id = ForeignIdColumn(foreign_key="controls.id")
    name = StringCol(nullable=False)
    description = StringCol(nullable=True)
    order_number = IntegerCol(nullable=True)

    control = relationship("Control", back_populates="sections")
    section_policies = relationship("SectionPolicy", back_populates="section")
