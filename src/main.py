#!/bin/python
from json import loads
from http.server import HTTPServer, BaseHTTPRequestHandler

import ebts_alarm
import ebts_message


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/getstate':
            body = str(ebts_alarm.get_state())

            self.send_response(200)
            self.send_header(
                "Content-type", "text/plain; charset=utf-8; version=0.0.4")
            self.end_headers()
            self.wfile.write(body.encode())

        else:
            body = "404 Not Found"
            self.send_response(404)
            self.end_headers()
            self.wfile.write(body.encode())

    def do_POST(self):
        if self.path == '/setstate':
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length)
            data = loads(body)
            body = str(ebts_alarm.set_state(data['state']))

            self.send_response(200)
            self.send_header(
                "Content-type", "text/plain; charset=utf-8; version=0.0.4")
            self.end_headers()
            self.wfile.write(body.encode())

        elif self.path == '/setmessage':
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length)
            data = loads(body)
            body = str(ebts_message.set_message(data['slot'], data['message']))

            self.send_response(200)
            self.send_header(
                "Content-type", "text/plain; charset=utf-8; version=0.0.4")
            self.end_headers()
            self.wfile.write(body.encode())

        else:
            body = "404 Not Found"
            self.send_response(404)
            self.end_headers()
            self.wfile.write(body.encode())


httpd = HTTPServer(('0.0.0.0', 8080), SimpleHTTPRequestHandler)
httpd.serve_forever()
