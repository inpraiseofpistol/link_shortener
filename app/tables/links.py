from sqlalchemy import Table, Column, String, ForeignKey, DateTime
from .base import id_, metadata
links = Table("links", metadata, id_(), Column("original_url", String, nullable=False), Column("short_code", String, unique=True, nullable=False), Column("user_id", ForeignKey("users.id"), nullable=False), Column("created_at", DateTime, nullable=False))