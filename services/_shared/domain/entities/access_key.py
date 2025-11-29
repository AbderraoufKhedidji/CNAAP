from sqlalchemy.orm import relationship
from _shared.domain.entities.bases.column_types import BoolCol, ForeignIdColumn, IdColumn, StringCol
from _shared.domain.entities.bases.entity_base import EntityBase

class AccessKey(EntityBase):
    __tablename__ = "access_keys"

    name = StringCol(nullable=False)
    status = BoolCol(default=True, nullable=True)

    # Relaciones
    role_id = ForeignIdColumn(foreign_key="roles.id")
    permission_group_id = ForeignIdColumn(foreign_key="permission_groups.id")

 





