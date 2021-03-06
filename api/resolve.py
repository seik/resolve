from datetime import datetime
from http.server import BaseHTTPRequestHandler
from urllib import parse

import requests
import validators


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        url = self.path[1:]
        valid_url = bool(validators.url(url))
        print(self.path)
        print(url)
        if not valid_url:
            self.send_response(400)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write("URL not valid".encode())
            return 

        r = requests.head(url, allow_redirects=True)

        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()

        self.wfile.write(r.url.encode())
        return
