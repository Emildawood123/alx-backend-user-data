#!/usr/bin/env python3
"""basic_auth moudle"""
from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """BasicAuth class"""
    pass
