from sqlalchemy.orm import relationship
from _shared.domain.entities.bases.column_types import IdColumn, StringCol
from _shared.domain.entities.bases.entity_base import EntityBase

class PermissionGroup(EntityBase):
    __tablename__ = "permission_groups"

    name = StringCol(nullable=False)
    type = StringCol(nullable=True)

    roles = relationship("Role", back_populates="permission_group")
