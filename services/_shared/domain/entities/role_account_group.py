from sqlalchemy.orm import relationship
from _shared.domain.entities.bases.column_types import ForeignIdColumn, IdColumn
from _shared.domain.entities.bases.entity_base import EntityBase

class RoleAccountsGroup(EntityBase):
    __tablename__ = "role_account_groups"

    role_id = ForeignIdColumn("roles.id")
    account_group_id = ForeignIdColumn("account_groups.id")

    role = relationship("roles", back_populates="accountGroups")
    account_group = relationship("accountGroups", back_populates="roles")
