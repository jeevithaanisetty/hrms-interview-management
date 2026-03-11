import uuid
from datetime import datetime
from sqlalchemy import Column, String, ForeignKey, Text, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.db.database import Base


class Candidate(Base):
    __tablename__ = "candidates"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    full_name = Column(String(150), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    phone = Column(String(20), nullable=True)
    position_applied = Column(String(150), nullable=False)
    department = Column(String(100), nullable=True)
    experience_years = Column(String(10), nullable=True)
    resume_url = Column(String(500), nullable=True)
    current_status = Column(String(50), default="Applied", nullable=False)
    source = Column(String(100), nullable=True)
    notes = Column(Text, nullable=True)
    created_by = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    created_by_user = relationship("User", foreign_keys=[created_by])
    interview_rounds = relationship("InterviewRound", back_populates="candidate", order_by="InterviewRound.round_number", cascade="all, delete-orphan")
    status_history = relationship("StatusHistory", back_populates="candidate", order_by="StatusHistory.changed_at", cascade="all, delete-orphan")
    audit_logs = relationship("AuditLog", back_populates="candidate", cascade="all, delete-orphan")