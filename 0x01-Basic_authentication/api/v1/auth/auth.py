#!/usr/bin/env python3
"""auth moudle"""
from flask import request as re
from typing import List, TypeVar


class Auth():
    """Auth class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require_auth method"""
        if path is not None:
            if path[-1] != '/':
                path += '/'
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path in excluded_paths:
            return False
        else:
            return True

    def authorization_header(self, request=None) -> str:
        """authorization_header"""
        if request is None or not 'Authorization' in request.headers:
            return None
        else:
            return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """current_user"""
        return None