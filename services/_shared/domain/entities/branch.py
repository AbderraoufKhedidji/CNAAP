import uuid
from sqlmodel import Field, Relationship
from .bases.entity_base import EntityBase
from .client import Client
from typing import Optional

class Branch(EntityBase, table=True):
    __tablename__ = "branches" # type: ignore

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, index=True)
    name: str = Field(..., description="Name of the branch")
    is_active: bool = Field(default=True)

    # Relations
    client_id: uuid.UUID = Field(..., foreign_key="clients.id", description="Parent client ID")
    client: Optional[Client] = Relationship()
