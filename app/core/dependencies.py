from fastapi import Depends
from app.core.security import get_mock_user

def get_current_user(user=Depends(get_mock_user)):
    return user