from sqlalchemy.orm import relationship
from _shared.domain.entities.bases.column_types import ForeignIdColumn, IdColumn
from _shared.domain.entities.bases.entity_base import EntityBase

class AccountAccountGroup(EntityBase):
    __tablename__ = "account_account_groups"

    account_id = ForeignIdColumn(foreign_key="cloud_accounts.id", nullable=False)
    account_group_id = ForeignIdColumn(foreign_key="account_groups.id", nullable=False)

    account = relationship("CloudAccounts", back_populates="account_groups")
    account_group = relationship("AccountGroup", back_populates="accounts")
