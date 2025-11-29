from sqlalchemy.orm import relationship
from _shared.domain.entities.bases.column_types import IdColumn
from _shared.domain.entities.bases.entity_base import EntityBase

class RoleGroup(EntityBase):
    __tablename__ = "rolegroup"

    role_id = IdColumn(primary_key=False, index=True)
    account_group_id = IdColumn(primary_key=False, index=True)

    role = relationship("Role", back_populates="account_groups")
    account_group = relationship("AccountGroup", back_populates="roles")
