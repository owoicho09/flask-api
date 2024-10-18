"""
blocklist.py

This file just contains the blocklist of the jet tokens. it will be imported by app and the logout resource so that
tokens can be added to the blocklist when the user logs out.
"""
from flask_sqlalchemy import SQLAlchemy

BLOCKLIST = SQLAlchemy()