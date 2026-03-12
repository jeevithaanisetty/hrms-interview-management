from fastapi import HTTPException, status
from datetime import datetime
from app.models.status_history import CandidateStatusHistory

ALLOWED_TRANSITIONS = {
    "Applied":["Interview Scheduled"],
    "Interview Scheduled": ["Interview Completed","Cancelled"],
    "Interview Completed": ["Selected","Rejected"],
}

def update_status(db,candidate,new_status,user):
    if new_status not in ALLOWED_TRANSITIONS.get(candidate.status,[]):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Invalid status transition")
    
    history=CandidateStatusHistory(
        candidate_id=candidate.id,
        old_status=candidate.status,
        new_status=new_status
    )

    candidate.status=new_status
    candidate.status_updated_at=datetime.utcnow()
    
    db.add(history)