#!/usr/bin/env python3
"""basic_auth moudle"""
from flask import request
from typing import List, TypeVar
from api.v1.auth.session_auth import SessionAuth
import base64
from models.user import User
import hashlib
from os import getenv
from datetime import timedelta, datetime


class SessionExpAuth(SessionAuth):
    """SessionExpAuth class"""
    def __init__(self):
        try:
            if getenv('SESSION_DURATION'):
                self.session_duration = int(getenv('SESSION_DURATION'))
            else:
                self.session_duration = 0
        except Exception:
            self.session_auth = 0

    def create_session(self, user_id=None):
        """create_session method"""
        try:
            session_id = super().create_session(user_id)
            if session_auth:
                self.user_id_by_session_id[session_id]['user_id'] = user_id
                self.user_id_by_session_id[session_id] = datetime.now()
                return session_id
            else:
                return None
        except Exception:
            return None

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """user_id_for_session_id"""
        if session_id is None:
            return None
        session_dictionary = self.user_id_by_session_id[session_id]
        if session_id not in self.user_id_by_session_id:
            return None
        if self.session_duration <= 0:
            return session_dictionary['user_id']
        if "created_at" not in session_dictionary:
            return None
        created_at = session_dictionary['created_at']
        if created_at is None:
            return None
        if (created_at + timedelta(seconds=self.session_duration)) \
                < datetime.now():
            return None
        return session_dictionary['user_id']
