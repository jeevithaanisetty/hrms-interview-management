from dotenv import load_dotenv
#from typing import Optional
from pydantic_settings import BaseSettings

load_dotenv()
class Settings(BaseSettings):
    DATABASE_URL:str
    SMTP_HOST:str="smtp.gmail.com"
    SMTP_PORT:int=587
    SMTP_USERNAME:str
    SMTP_PASSWORD:str
    SMTP_SENDER:str

settings=Settings()