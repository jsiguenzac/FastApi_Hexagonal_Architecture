from pydantic import BaseModel, EmailStr
from typing import Optional

class UserSchema(BaseModel):
    name: str
    last_name: str
    email: EmailStr
    phone: Optional[str] = None
    
class UserCreateSchema(UserSchema):
    password: str
    
class UserFindSchema(UserSchema):
    id_user: int