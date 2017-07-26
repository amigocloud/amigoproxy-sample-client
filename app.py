from __future__ import print_function
import sys
import logging
import time

from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def base():
    if request.method == 'POST':
        time.sleep(1)
        return 'Received the following data: %s' % request.data
    else:
        return 'Proxy Test Server is working.'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
