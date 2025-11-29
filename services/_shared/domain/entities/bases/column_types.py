# services/_shared/domain/entities/column_types.py
import uuid
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean, Time

# UUID genérico compatible con cualquier base
def gen_uuid() -> str:
    return str(uuid.uuid4())

Id = String(36)          # Para cualquier motor

def IdColumn(primary_key=True, index=True):
    return Column(Id, primary_key=primary_key, index=index)

def ForeignIdColumn(foreign_key, nullable=False, index=True):
    return Column(String(36), ForeignKey(foreign_key), nullable=nullable, index=index)

# Column shortcuts
IntegerCol = lambda **kwargs: Column(Integer, **kwargs)
DateTimeCol = lambda **kwargs: Column(DateTime, **kwargs)
StringCol = lambda length=255, **kwargs: Column(String(length), **kwargs)
BoolCol = lambda **kwargs: Column(Boolean, **kwargs)
TimeCol = lambda **kwargs: Column(Time, **kwargs)
