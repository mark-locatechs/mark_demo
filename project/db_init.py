#!/usr/bin/env python

from app.app import app
from app.models import database_init

import time


# reset DB
with app.app_context():

    print('wait for db')

    time.sleep(2)

    database_init()

print('db init completed')

