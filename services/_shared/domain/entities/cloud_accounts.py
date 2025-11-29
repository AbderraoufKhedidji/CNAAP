from sqlalchemy.orm import relationship
from _shared.domain.entities.bases.column_types import ForeignIdColumn, IdColumn, StringCol
from _shared.domain.entities.bases.entity_base import EntityBase

class CloudAccounts(EntityBase):
    __tablename__ = "cloud_accounts"

    tenant_id = ForeignIdColumn(foreign_key="tenant_info.id")
    cloud_type = StringCol(nullable=False)
    name = StringCol(nullable=False)
    account_type = StringCol(nullable=False)
    
    tenant = relationship("TenantInfo", back_populates="cloud_accounts")
    account_groups = relationship("AccountAccountGroup", back_populates="account")
