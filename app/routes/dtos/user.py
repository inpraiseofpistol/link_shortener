# dtos/user.py
from pydantic import BaseModel, EmailStr
class RegisterUserDTO(BaseModel): email: EmailStr; password: str
class ShowUserDTO(BaseModel): id: int; email: EmailStr