#!/usr/bin/env python3
"""encrypt_password"""
import bcrypt


def hash_password(password: str) -> bytes:
    """hash_password method"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
def is_valid(hashed_password: bytes, password: str) -> bool:
    """is_valid method"""
    return bcrypt.checkpw(password, hashed_password)
