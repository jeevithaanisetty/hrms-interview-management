# app/models/status_history.py

import uuid
from sqlalchemy import Column, String, ForeignKey, Text, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.database import Base








class StatusHistory(Base):
    __tablename__ = "status_history"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)





    # Which candidate this status change belongs to
    candidate_id = Column(
        UUID(as_uuid=True),
        ForeignKey("candidates.id", ondelete="CASCADE"),
        nullable=False
    )




    # The status values — e.g. "Applied" → "Interview Scheduled" → "Selected"
    previous_status = Column(String(50), nullable=True)   # null on first status set
    new_status = Column(String(50), nullable=False)






    # Optional: which interview round triggered this change

    interview_round_id = Column(
        UUID(as_uuid=True),
        ForeignKey("interview_rounds.id", ondelete="SET NULL"),
        nullable=True
    )

    # Why the status changed (reschedule reason, cancellation reason, etc.)


    remarks = Column(Text, nullable=True)

    # Who made the change
    changed_by = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True
    )

    changed_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)





    # Relationship




    candidate = relationship("Candidate", back_populates="status_history")
    changed_by_user = relationship("User", foreign_keys=[changed_by])
    interview_round = relationship("InterviewRound", foreign_keys=[interview_round_id])