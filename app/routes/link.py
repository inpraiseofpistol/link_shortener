from fastapi import APIRouter, Response
from dishka.integrations.fastapi import FromDishka, DishkaRoute
from app.entities import Link
from app.repositories.link import LinkRepository
from app.services.shortener import ShortenerService
from app.errors import LinkNotFound
from .dtos.link import CreateLinkDTO, ShowLinkDTO

link_router = APIRouter(prefix="/links", tags=["Links"], route_class=DishkaRoute)

@link_router.post("")
async def create(dto: CreateLinkDTO, svc: FromDishka[ShortenerService], repo: FromDishka[LinkRepository]) -> ShowLinkDTO:
    # Для простоты привязываем к пользователю с id=1
    link = Link(original_url=str(dto.original_url), short_code=await svc.generate_unique_code(), user_id=1)
    await repo.create(link)
    return link

@link_router.get("/{code}")
async def redirect(code: str, repo: FromDishka[LinkRepository]) -> Response:
    link = await repo.get_by_code(code)
    if not link: raise LinkNotFound("Link not found")
    return Response(status_code=301, headers={"Location": link.original_url})