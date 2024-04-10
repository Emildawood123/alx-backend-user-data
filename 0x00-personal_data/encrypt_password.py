#!/usr/bin/env python3
"""
encrypt_password
"""
import bcrypt
from typing import ByteString

def hash_password(password: str) -> ByteString:
    """hash_password method"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
