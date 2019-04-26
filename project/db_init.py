#!/usr/bin/env python

from app.app import app
from app.models import database_init


# reset DB
with app.app_context():
    database_init()

