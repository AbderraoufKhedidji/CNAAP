from pydantic import BaseModel
from typing import Generic, TypeVar, List, Optional

T = TypeVar("T")

class ListResponse(Generic[T], BaseModel):
    success: bool = True
    total: int
    items: List[T]

class GetResponse(Generic[T], BaseModel):
    success: bool = True
    item: Optional[T] = None

class MessageResponse(BaseModel):
    success: bool = True
    message: str

class CreateResponse(MessageResponse):
    message: str = "Item created successfully"

class UpdateResponse(MessageResponse):
    message: str = "Item updated successfully"

class DeleteResponse(MessageResponse):
    message: str = "Item deleted successfully"
