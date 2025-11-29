from sqlalchemy.orm import relationship
from _shared.domain.entities.bases.column_types import ForeignIdColumn, IdColumn, StringCol, DateTimeCol, TimeCol
from _shared.domain.entities.bases.entity_base import EntityBase

class Event(EntityBase):
    __tablename__ = "event"

    event_time = DateTimeCol(nullable=False) 
    account_name = StringCol(nullable=True)  
    region = StringCol(nullable=True)  
    snoozed_for = StringCol(nullable=True)  
    snoozed_expired = TimeCol(nullable=True)  
    reason = StringCol(nullable=True)  
    account_owners = StringCol(nullable=True)  
    
    #asset_id = ForeignIdColumn("assets.id")
    #account_id = ForeignIdColumn("accounts.id")
    #region_id = ForeignIdColumn("regions.id") 

    assets = relationship("AssetName", back_populates="events")  
    event_alerts = relationship("EventAlert", back_populates="events")
