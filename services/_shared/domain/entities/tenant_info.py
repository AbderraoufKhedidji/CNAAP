from typing import Optional
from sqlalchemy.orm import relationship
from _shared.domain.entities.bases.column_types import IdColumn, StringCol, BoolCol, DateTimeCol
from _shared.domain.entities.bases.entity_base import EntityBase

class TenantInfo(EntityBase):
    __tablename__ = "tenant_info"

    cloud_type = StringCol()
    name = StringCol()
    tenant_type = StringCol()
    status = StringCol()
    cloud_account_owner = StringCol()
    cloud_account_enabled = BoolCol()

    cloud_accounts = relationship("CloudAccounts", back_populates="tenant")
