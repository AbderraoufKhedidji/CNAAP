from sqlalchemy.orm import relationship
from _shared.domain.entities.bases.column_types import ForeignIdColumn, IdColumn, StringCol, BoolCol
from _shared.domain.entities.bases.entity_base import EntityBase

class Role(EntityBase):
    __tablename__ = "roles"

    name = StringCol(nullable=False)
    permission_group_id = ForeignIdColumn(foreign_key="permission_groups.id")
    alert_dismissal_restricted = BoolCol(nullable=True)
    description = StringCol(nullable=True)
    only_allow_compute_capabilities = StringCol(nullable=True)
    resource_lists = StringCol(nullable=True)
    on_prem_other_cloud_providers = StringCol(nullable=True)

    account_groups = relationship("RoleAccountGroup", back_populates="role")
    users = relationship("RoleUsers", back_populates="role")
    access_keys = relationship("AccessKey", back_populates="role_ref") 
