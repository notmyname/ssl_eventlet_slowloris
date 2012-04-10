#!/usr/bin/env python

from eventlet import wsgi
import eventlet

resp_body = 'x' * (1024 * 653 + 34)  # 668706


def hello_world(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return [resp_body]

wsgi.server(eventlet.wrap_ssl(eventlet.listen(('', 8090)),
                              certfile='/etc/ssl/example.crt',
                              keyfile='/etc/ssl/example.key',
                              server_side=True),
            hello_world)
