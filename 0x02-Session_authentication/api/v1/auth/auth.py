#!/usr/bin/env python3
"""auth moudle"""
from flask import request
from typing import List, TypeVar
from os import getenv


class Auth():
    """Auth class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require_auth method"""
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path is not None:
            if path[-1] != '/':
                path += '/'
            for ex_path in excluded_paths:
                if ex_path[-1] == '*':
                    if ex_path[:-1] in path:
                        return False
                elif ex_path[-1] != '*':
                    if ex_path == path:
                        return False
            return True

    def authorization_header(self, request=None) -> str:
        """authorization_header"""
        if request is None or 'Authorization' not in request.headers:
            return None
        else:
            return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """current_user"""
        return None

    def session_cookie(self, request=None):
        """session_cookie"""
        if request is None:
            return None
        else:
            return request.cookies.get(getenv('SESSION_NAME'))
