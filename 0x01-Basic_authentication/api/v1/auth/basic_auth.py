#!/usr/bin/env python3
"""basic_auth moudle"""
from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth
import base64
from models.user import User
import hashlib


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

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """extract_user_credentials method"""
        if decoded_base64_authorization_header is None:
            return None, None
        if type(decoded_base64_authorization_header) != str:
            return None, None
        if decoded_base64_authorization_header.find(':') == -1:
            return None, None
        else:
            if len(decoded_base64_authorization_header) == 1:
                return '', ''
            else:
                my_lst = decoded_base64_authorization_header.split(':')
                user = my_lst[0]
                passwd = my_lst[1]
                return user, passwd
            
    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """user_object_from_credentials method"""
        if user_email is None or type(user_email) != str:
            return None
        if user_pwd is None or type(user_pwd) != str:
            return None
        if User.search({'email': user_email}) == []:
            return None
        else:
            pass_after_hash = hashlib.sha256(user_pwd.encode()).hexdigest().lower()
            if User.search({'email': user_email})[-1].password == pass_after_hash:
                return User.search({'email': user_email})[-1]
            else:
                return None
