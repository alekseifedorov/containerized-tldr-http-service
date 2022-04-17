from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
import subprocess


class HttpGetHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("GET " + self.path)
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        result = subprocess.run(['tldr', self.path], stdout=subprocess.PIPE)
        self.wfile.write(result.stdout)
        self.wfile.flush()


def run(server_class=HTTPServer, handler_class=HttpGetHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print("Starting httpd server")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()


run()
