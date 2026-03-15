from fastapi import Depends, HTTPException, status
from typing import List
from app.core.dependencies import get_current_user

class RoleChecker:
    def __init__(self, allowed_roles: List[str]):
        self.allowed_roles=allowed_roles
    
    def __call__(self, user=Depends(get_current_user)):
        if user.role not in self.allowed_roles:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Access denied")
        return user

allow_view=RoleChecker(["admin","hr_manager","hr_executive","viewer"])
allow_schedule=RoleChecker(["admin","hr_manager","hr_executive"])
allow_feedback= RoleChecker({"admin","hr_manager","hr_executive"})
allow_cancel=RoleChecker(["admin","hr_manager"])