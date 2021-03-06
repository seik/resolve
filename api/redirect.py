from datetime import datetime
from http.server import BaseHTTPRequestHandler
from urllib import parse

import requests
import validators


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        params = dict(parse.parse_qsl(parse.urlsplit(self.path).query))
        valid_url = bool(validators.url(params.get("url", "")))

        if not valid_url:
            self.send_response(400)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write("URL not valid".encode())
            return 

        r = requests.head(params["url"], allow_redirects=True)

        self.send_response(302)
        self.send_header("Location", r.url)
        self.end_headers()

        return
