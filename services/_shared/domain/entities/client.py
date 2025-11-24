import uuid
from sqlmodel import Field
from .bases.entity_base import EntityBase

class Client(EntityBase, table=True):
    __tablename__ = "clients" # type: ignore

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, index=True)
    name: str = Field(..., description="Name of the company/client")
    is_active: bool = Field(default=True)
