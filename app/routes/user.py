from fastapi import APIRouter
from dishka.integrations.fastapi import FromDishka, DishkaRoute
from passlib.context import CryptContext
from app.entities import User
from app.repositories.user import UserRepository
from app.errors import UserAlreadyExists
from .dtos.user import RegisterUserDTO, ShowUserDTO

pwd = CryptContext(schemes=["bcrypt"], deprecated="auto")
user_router = APIRouter(prefix="/users", tags=["Users"], route_class=DishkaRoute)

@user_router.post("/register")
async def register(dto: RegisterUserDTO, repo: FromDishka[UserRepository]) -> ShowUserDTO:
    if await repo.get_by_email(dto.email): raise UserAlreadyExists("User exists")
    user = User(email=dto.email, password_hash=pwd.hash(dto.password))
    await repo.create(user)
    return user

