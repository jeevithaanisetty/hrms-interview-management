from datetime import datetime  
from app.db.database import SessionLocal
from app.models.interview import InterviewRound
from app.services.notification_service import NotificationService

def check_and_send_reminder():
    db=SessionLocal()
    try:
        now=datetime.utcnow()
        interviews=db.query(InterviewRound).filter(InterviewRound.status=="Scheduled").all()
        for interview in interviews:
            diff_hours=(interview.scheduled_date-now).total_seconds()/3600
            
            if 23.5< diff_hours<=24 and not interview.reminder_24_hrs:
                NotificationService.send_reminder(interview.candidate, interview)
                interview.reminder_24_hrs=True
            if 0.5< diff_hours <=1 and not interview.reminder_1_hr:
                NotificationService.send_reminder(interview.candidate, interview)
                interview.reminder_1_hr=True
            db.commit()
    except Exception as e:
        db.rollback()
        print(f"Error sending Reminders: {e}")
    finally:
        db.close()
            