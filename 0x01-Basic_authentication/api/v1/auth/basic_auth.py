#!/usr/bin/env python3
"""basic_auth moudle"""
from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """BasicAuth class"""
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """extract_base64_authorization_header method"""
        if authorization_header is None:
            return None
        if type(authorization_header) != str:
            return None
        if len(authorization_header) > 6:
            if authorization_header[:6] == 'Basic ':
                return authorization_header.split(' ')[1]
        else:
            return None

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """decode_base64_authorization_header method"""
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) != str:
            return None
        try:
            r = base64.b64decode(base64_authorization_header)
            return r.decode('utf-8')
        except Exception:
            return None
