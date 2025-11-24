import uuid
from sqlmodel import Field, Relationship
from .bases.entity_base import EntityBase
from .branch import Branch
from typing import Optional

class User(EntityBase, table=True):
    __tablename__ = "users" # type: ignore

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, index=True)
    name: str = Field(..., description="Full name of the user")
    email: str = Field(..., unique=True, index=True, description="Email address")
    hashed_password: str = Field(..., description="Hashed password")
    is_active: bool = Field(default=True)
    is_superuser: bool = Field(default=False)

    # Relations
    branch_id: uuid.UUID = Field(..., foreign_key="branches.id", description="Branch ID of the user")
    branch: Optional[Branch] = Relationship()
