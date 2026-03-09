# app/models/candidate.py

import uuid
from sqlalchemy import Column, String, ForeignKey, Text, TIMESTAMP, Date
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.database import Base


class Candidate(Base):
    __tablename__ = "candidates"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    # Basic Info
    full_name = Column(String(150), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    phone = Column(String(20), nullable=True)
    
    # Job Info
    position_applied = Column(String(150), nullable=False)
    department = Column(String(100), nullable=True)
    experience_years = Column(String(10), nullable=True)  # e.g. "3-5"
    resume_url = Column(String(500), nullable=True)
    
    # Current Status
    current_status = Column(String(50), default="Applied", nullable=False)
    # Possible values: Applied, Screening, Interview Scheduled, 
    # Interview In Progress, Selected, Rejected, On Hold

    # Source of candidate
    source = Column(String(100), nullable=True)  # e.g. LinkedIn, Referral, Job Portal

    # Extra
    notes = Column(Text, nullable=True)

    # Who added this candidate
    created_by = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True
    )

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())

    # Relationships
    created_by_user = relationship("User", foreign_keys=[created_by])
    
    interview_rounds = relationship(
        "InterviewRound",
        back_populates="candidate",
        order_by="InterviewRound.round_number",
        cascade="all, delete-orphan"
    )
    
    status_history = relationship(
        "StatusHistory",
        back_populates="candidate",
        order_by="StatusHistory.changed_at",
        cascade="all, delete-orphan"
    )
    
    audit_logs = relationship(
        "AuditLog",
        back_populates="candidate",
        cascade="all, delete-orphan"
    )