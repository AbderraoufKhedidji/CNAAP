from sqlalchemy.orm import relationship
from _shared.domain.entities.bases.column_types import DateTimeCol, IdColumn, StringCol
from _shared.domain.entities.bases.entity_base import EntityBase

class AccountGroup(EntityBase):
    __tablename__ = "account_groups"

    name = StringCol(nullable=False)
    description = StringCol(nullable=True)
    last_modified_by = StringCol(nullable=True)
    last_modified_on = DateTimeCol(nullable=True)

    # Relaciones
    accounts = relationship("AccountAccountGroup", back_populates="account_group")
    roles = relationship("RoleAccountsGroup", back_populates="account_group")
