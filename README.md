# AmigoProxy Sample Client
This is a sample client for listening to AmigoProxy Requests

Just clone the project, make sure you have docker and docker-compose installed and run:

`docker-compose build`
`docker-compose up -d` or `docker-compose up` if you don't want it as a daemon

Usage:

You can set the server address (provided it is internet visible) of wherever you deploy this as a target for AmigoProxy. When a POST request is made against this server it will store the latest value sent to it and the time.

If you do a GET request against this server it will return the latest value sent to it as well as the number of seconds since the last POST to it. If this number exceeds a max value (300 seconds by default) the response will be a string indicating the server is not receiving data. This max value is the variable `MAX_INACTIVE_SECONDS` and you can change it in `app.py`.
