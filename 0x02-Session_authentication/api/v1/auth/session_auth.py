#!/usr/bin/env python3
"""SessionAuth moudle"""
from flask import request, jsonify
from typing import List, TypeVar
from api.v1.auth.auth import Auth
import base64
from models.user import User
import hashlib
import uuid
from api.v1.views import app_views


class SessionAuth(Auth):
    """SessionAuth class"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """create_session method"""
        if user_id is None or type(user_id) is not str:
            return None
        else:
            session_id = uuid.uuid4()
            self.user_id_by_session_id[session_id] = user_id
            return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """user_is_for_session_id method"""
        if session_id is None:
            return None
        try:
            return self.user_id_by_session_id.get(session_id)
        except Exception:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """current_user overload method"""
        cookie = self.session_cookie(request)
        user_id = self.user_id_for_session_id(str(cookie))
        return User.get(user_id)

    def destroy_session(self, request=None):
        """"destroy_session"""
        if request is None:
            return False
        get_cookie = self.session_cookie(request)
        if get_cookie is None:
            return False
        if self.user_id_for_session_id(get_cookie) is None:
            return False
        else:
            del user_id_by_session_id[get_cookie]
            return True
