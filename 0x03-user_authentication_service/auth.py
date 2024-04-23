#!/usr/bin/env python3
"""Auth module."""
import bcrypt
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from user import User
import uuid


def _hash_password(password: str) -> bytes:
    """_hash_password method that return bytes."""
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

