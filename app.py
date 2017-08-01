from __future__ import print_function
import sys
import logging
import time
import threading
import datetime

import redis
from flask import Flask, request

app = Flask(__name__)

# This is the amount of seconds between events before an alert is triggered
MAX_INACTIVE_SECONDS = 300

REDIS_HOST = 'redis'
REDIS_PORT = 6379
REDIS_SERVER = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT)

REDIS_SERVER.set('last_value', 'Nothing yet')
REDIS_SERVER.set('last_save', datetime.datetime.now())

@app.route('/', methods=['GET', 'POST'])
def base():
    if request.method == 'POST':
        # Modify this timeout value in order to emulate some processing on
        # a target
        REDIS_SERVER.set('last_value', request.data)
        REDIS_SERVER.set('last_save', datetime.datetime.now())
        time.sleep(1)
        return 'Received the following data: %s' % request.data
    else:
        last_save = datetime.datetime.strptime(
            REDIS_SERVER.get('last_save'),
            '%Y-%m-%d %H:%M:%S.%f'
        )
        now = datetime.datetime.now()
        time_diff = (now - last_save).seconds

        if time_diff < MAX_INACTIVE_SECONDS:
            return ('Last value: %s' +\
                ' Seconds since last save %s') % (
                REDIS_SERVER.get('last_value'), time_diff)
        else:
            # This string will be returned if it looks like no proxy requests
            # are coming in
            return 'Proxy not responding.'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
