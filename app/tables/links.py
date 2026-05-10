from sqlalchemy import Table, Column, String, DateTime
from .base import id_, metadata

links = Table(
    "links", metadata, id_(),
    Column("original_url", String, nullable=False),
    Column("short_code", String, unique=True, nullable=False),
    Column("created_at", DateTime(timezone=True), nullable=False)
)