#!/usr/bin/env python3
"""basic_auth moudle"""
from flask import request
from typing import List, TypeVar
from api.v1.auth.session_auth import SessionAuth
import base64
from models.user import User
import hashlib
from os import getenv
import datetime


class SessionExpAuth(SessionAuth):
    """SessionExpAuth class"""
    def __init__(self):
        try:
            self.session_duration = getenv('SESSION_DURATION')
        except Exception:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """create_session method"""
        try:
            session_id = super().create_session(user_id)
            if session_id is None:
                return None
            self.user_id_by_session_id[session_id]['user_id'] = user_id
            self.user_id_by_session_id[session_id] = datetime.now()
            return session_id
        except Exception:
            return None
