import uuid
from sqlalchemy import Column, String, Integer, ForeignKey, Text, TIMESTAMP, Boolean, CheckConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.database import Base

class InterviewRound(Base):
    __tablename__ = "interview_rounds"
 
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    candidate_id = Column(UUID(as_uuid=True), ForeignKey("candidates.id", ondelete="CASCADE"), nullable=False)
    round_number = Column(Integer, nullable=False)
    round_type = Column(String(50), nullable=False)
    scheduled_date = Column(TIMESTAMP, nullable=True)
    duration_minutes = Column(Integer, default=60)
    interviewer_name = Column(String(100), nullable=True)
    interviewer_email = Column(String(255), nullable=True)
    meeting_link = Column(String(500), nullable=True)
    status = Column(String(30), default="scheduled")
    feedback = Column(Text, nullable=True)
    rating = Column(Integer)
    recommendation = Column(String(20), nullable=True)
    created_by = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=True)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
    __table_args__ = (CheckConstraint("rating >= 1 AND rating <= 5", name="check_rating_range"),)
    reminder_24_hrs = Column(Boolean, default=False)
    reminder_1_hr = Column(Boolean, default=False)
    
    candidate = relationship("Candidate", back_populates="interview_rounds")