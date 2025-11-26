from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional
from uuid import UUID

class EntityBase(SQLModel):
    created_at: datetime = Field(default_factory=datetime.utcnow, description="Creation timestamp")
    updated_at: datetime = Field(default_factory=datetime.utcnow, description="Last update timestamp")
    created_by: Optional[UUID] = Field(None, description="User ID who created the record")
    updated_by: Optional[UUID] = Field(None, description="User ID who last updated the record")
    is_deleted: Optional[bool] = Field(False, description="User ID who last updated the record")
