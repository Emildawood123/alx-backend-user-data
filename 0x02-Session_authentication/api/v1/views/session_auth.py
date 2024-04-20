#!/usr/bin/env python3
""" Module of Index views
"""
from flask import jsonify, abort, request
from api.v1.views import app_views
from models.user import User


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
