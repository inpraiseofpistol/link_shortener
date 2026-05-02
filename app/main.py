from contextlib import asynccontextmanager
from fastapi import FastAPI, APIRouter
from fastapi.responses import JSONResponse
from dishka.integrations.fastapi import setup_dishka
from sqlalchemy.orm import registry
from app.errors import HandlingError
from app.container import container
from app.routes.user import user_router
from app.routes.link import link_router
from app.entities import User, Link
from app.tables import users, links

def map_tables():
    reg = registry()
    reg.map_imperatively(User, users)
    reg.map_imperatively(Link, links)

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.include_router(APIRouter(prefix="/api/v1", routes=[*user_router.routes, *link_router.routes]))
    map_tables()
    yield
    await container.close()

app = FastAPI(lifespan=lifespan)
setup_dishka(container, app)

@app.exception_handler(HandlingError)
async def handle_err(req, err: HandlingError):
    return JSONResponse({"detail": str(err)}, status_code=err.status)