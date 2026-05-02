# tables/users.py
from sqlalchemy import Table, Column, String
from .base import id_, metadata
users = Table("users", metadata, id_(), Column("email", String, unique=True, nullable=False), Column("password_hash", String, nullable=False))
