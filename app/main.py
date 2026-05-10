from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from dishka.integrations.fastapi import setup_dishka
from sqlalchemy.orm import registry
from app.errors import HandlingError
from app.container import container
from app.routes.link import link_router
from app.entities.link import Link
from app.tables.links import links

def map_tables():
    reg = registry()
    reg.map_imperatively(Link, links)

@asynccontextmanager
async def lifespan(app: FastAPI):
    map_tables()
    app.include_router(link_router)
    yield
    await container.close()

app = FastAPI(lifespan=lifespan)
setup_dishka(container, app)

@app.exception_handler(HandlingError)
async def handle_err(req, err: HandlingError):
    return JSONResponse({"detail": str(err)}, status_code=err.status)