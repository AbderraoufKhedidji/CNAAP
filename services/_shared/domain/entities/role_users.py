from sqlalchemy.orm import relationship
from _shared.domain.entities.bases.column_types import ForeignIdColumn, IdColumn
from _shared.domain.entities.bases.entity_base import EntityBase

class RoleUsers(EntityBase):
    __tablename__ = "role_users"

    role_id = ForeignIdColumn("roles.id")
    user_id = ForeignIdColumn("users.id")


    role = relationship("Role", back_populates="users")
    user = relationship("User", back_populates="roles")
