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

    def current_user(self, request=None):
        """current_user overload method"""
        cookie = self.session_cookie(request)
        user_id = self.user_id_for_session_id(cookie)
        return User.get(user_id)

    @app_views.route('/auth_session/login', methods=['POST'],
                     strict_slashes=False)
    def session_route() -> str:
        try:
            email = request.form.get('email')
            if email == '' or email is None:
                return jsonify({"error": "email missing"}), 400
        except Exception:
            return jsonify({"error": "email missing"}), 400
        try:
            password = request.form.get('password')
            if password == '' or password is None:
                return jsonify({"error": "password missing"}), 400
        except Exception:
            return jsonify({"error": "password missing"}), 400
        get_user = User.search({'email': email})
        if get_user == []:
            return jsonify({"error": "no user found for this email"}), 404
        else:
            if not get_user[-1].is_valid_password(password):
                return jsonify({"error": "wrong password"}), 401
            else:
                from api.v1.app import auth
                return (get_user[-1]).to_json()
