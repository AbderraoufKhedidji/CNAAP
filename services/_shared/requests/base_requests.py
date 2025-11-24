from uuid import UUID
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class BaseRequest(BaseModel):
    request_id: Optional[str] = Field(None, description="Unique request ID")
    timestamp: Optional[datetime] = Field(None, description="Request timestamp")

class CreateRequest(BaseRequest):
    # Los campos específicos se agregan en cada recurso
    pass

class UpdateRequest(BaseRequest):
    id: UUID = Field(..., description="ID del recurso a actualizar")

class DeleteRequest(BaseRequest):
    id: UUID = Field(..., description="ID del recurso a eliminar")

class GetRequest(BaseRequest):
    id: UUID = Field(..., description="ID del recurso a obtener")

class SearchRequest(BaseRequest):
    query: Optional[str] = Field(None, description="Search term")
    limit: Optional[int] = Field(10, description="Maximum number of results")
    offset: Optional[int] = Field(0, description="Pagination offset")