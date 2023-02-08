#!/usr/bin/env python3
"""
Manage API authentication
"""
from flask import request
from typing import List, TypeVar


class Auth():
    """
    Manage API authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ require authentication """
        if path is None or excluded_paths is None or not len(excluded_paths):
            return True
        if path[-1] != '/':
            path += '/'
        if excluded_paths[-1] != '/':
            excluded_paths += '/'
        asters = [stars[:-1]
                  for stars in excluded_paths if stars[-1] == '*']

        for starts in asters:
            if path.startswith(stars):
                return False
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """ authorization header """
        if request is None:
            return None
        if 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """ current user """
        return None
