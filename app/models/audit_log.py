from sqlalchemy import Column,String,DateTime,Text,ForeignKey 
from sqlalchemy.dialects.postgresql import UUID,JSONB 
from sqlalchemy.orm import relationship 
from db.database import Base 
from datetime import datetime 
import uuid 


class AuditLog(Base):
    
    __tablename__="audit_logs"
    
    id = Column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4)
    user_id = Column(UUID,nullable=False)   #who performed action 
    entity_type = Column(String,nullable=False) 
    entity_id = Column(UUID,nullable=False)
    action = Column(String,nullable=False)    
    old_values = Column(JSONB,nullable=True)
    new_values = Column(JSONB,nullable=True)
    description = Column(Text,nullable=True) 
    created_at = Column(DateTime,default=datetime.utcnow)