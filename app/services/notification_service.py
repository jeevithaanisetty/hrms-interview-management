import smtplib
from email.mime.text import MIMEText
from app.config import settings

class NotificationService:
    @staticmethod
    def send_email(to_email,subject,body):
        msg=MIMEText(body)
        msg["Subject"]=subject
        msg["From"]= settings.SMTP_SENDER
        msg["To"]=to_email
        try:
            server=smtplib.SMTP(settings.SMTP_HOST,settings.SMTP_PORT)
            server.starttls()
            server.login(settings.SMTP_USERNAME,settings.SMTP_PASSWORD)
            server.send_message(msg)
            server.quit()
        except Exception as e :
            print("Email Sending Failed:",e)
        
    @staticmethod
    def send_schedule(candidate,interview):
        NotificationService.send_email(candidate.email,
                                       "Interview Scheduled",
                                       f"Interview scheduled at {interview.scheduled_date} \n Link:{interview.meeting_link}")
        
    @staticmethod
    def send_reschedule(candidate,interview):
        NotificationService.send_email(candidate.email,
                                       "Interview Rescheduled",
                                       f"Interview rescheduled at {interview.scheduled_date} \n Link:{interview.meeting_link}")
    @staticmethod
    def send_cancelled(candidate,interview):
        NotificationService.send_email(candidate.email,
                                       "Interview Cancelled",
                                       f"Interview on {interview.scheduled_date} cancelled")
        
    @staticmethod
    def send_feedback(candidate,interview):
        NotificationService.send_email(settings.SMTP_USERNAME,
                                       "Interview feedback Submitted",
                                       f"Candidate:{candidate.first_name}\n Rating:{interview.rating}")
        
    @staticmethod
    def send_reminder(candidate,interview):
        NotificationService.send_email(candidate.email,
                                       "Interview Reminder",
                                       f"Reminder: Interview at {interview.scheduled_date}")
        