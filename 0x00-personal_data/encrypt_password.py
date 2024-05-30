#!/usr/bin/env python3
"""Defines a hash password function to return a hashed password"""
import bcrypt
from bcrypt import hashpw


def hash_password(password, str) -> bytes:
    """Returns a hash password"""
    b = password.encode()
    hashed = hashpw(b, bcrypt.gensalt())
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Check if the password is valid"""
    return bcrypt.is_valid(password.encode(), hashed_password)
