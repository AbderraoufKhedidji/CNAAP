from typing import Optional, List
from sqlalchemy.orm import relationship
from _shared.domain.entities.bases.column_types import ForeignIdColumn, IdColumn, IntegerCol, StringCol, BoolCol, DateTimeCol
from _shared.domain.entities.bases.entity_base import EntityBase

class User(EntityBase):
    __tablename__ = "users"

    username = StringCol()
    name = StringCol()
    age = IntegerCol()
    type = StringCol()
    default_role = StringCol()
    permissions_group = StringCol()
    user_type = StringCol()
    access_key_allowed = StringCol()
    last_login_time = DateTimeCol()
    role_id = ForeignIdColumn(foreign_key="roles.id")

    roles = relationship("RoleUsers", back_populates="user")
