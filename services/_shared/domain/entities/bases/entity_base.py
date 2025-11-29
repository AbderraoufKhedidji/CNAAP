from datetime import datetime
from sqlalchemy import Column, Boolean, DateTime
from .column_types import IdColumn
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class EntityBase(Base):
    __abstract__ = True

    id = IdColumn()
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    created_by = IdColumn(primary_key=False)
    updated_by = IdColumn(primary_key=False)
    is_deleted = Column(Boolean, default=False, nullable=False)

    @classmethod
    def __declare_last__(cls):
        if not hasattr(cls, "__tablename__") or cls.__tablename__ is None:
            cls.__tablename__ = cls.__name__.lower()