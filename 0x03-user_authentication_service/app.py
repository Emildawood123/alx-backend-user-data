#!/usr/bin/env python3
"""app model
"""
from flask import Flask, jsonify, request, abort, make_response, redirect
from auth import Auth
from sqlalchemy.orm.exc import NoResultFound

AUTH = Auth()
app = Flask(__name__)


@app.route('/', methods=['GET'])
def root_route():
    """root_route method"""
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def regester_user_verify():
    """regester_user_verify method"""
    email = request.form['email']
    password = request.form['password']
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": f"{email}", "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"})


@app.route('/sessions', methods=['POST'])
def login():
    """login method"""
    email = request.form['email']
    password = request.form['password']
    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        response = make_response(
            jsonify({"email": email, "message": "logged in"}), 200)
        response.set_cookie("session_id", session_id)
        return response
    else:
        return abort(401)


@app.route('/sessions', methods=['DELETE'])
def logout(request):
    """logout method"""
    cookies = request.cookies
    session_id = cookies['session_id']
    try:
        user = AUTH.get_user_from_session_id(session_id)
        AUTH.destroy_session(user.id)
        return redirect('localhost:5000/')
    except NoResultFound:
        return abort(403)


@app.route('/profile', methods=['GET'])
def profile():
    """profile method"""
    try:
        session_id = request.cookies.get('session_id')
        user = AUTH.get_user_from_session_id(session_id)
        if user:
            return jsonify({"email": user.email}), 200
        return abort(403)
    except NoResultFound:
        return abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
