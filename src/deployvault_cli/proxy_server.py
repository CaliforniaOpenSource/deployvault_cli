from http.server import HTTPServer, SimpleHTTPRequestHandler
import requests
import threading
import os

class ProxyHTTPRequestHandler(SimpleHTTPRequestHandler):
    token = ""
    repo_url = ""

    def do_GET(self):
        url = f"{self.repo_url}{self.path}"
        headers = {"Authorization": f"Bearer {self.token}"}
        print("proxy headers: ",headers)
        response = requests.get(url, headers=headers)
        
        self.send_response(response.status_code)
        #for key, value in response.headers.items():
        #    self.send_header(key, value)
        if self.is_likely_package_listing(self.path):
            self.send_header("Content-type", "text/html")
        else:
            self.send_header("Content-type", response.headers.get('Content-Type', 'application/octet-stream'))

        
        self.end_headers()
        self.wfile.write(response.content)

    def is_likely_package_listing(self, path):
        # TODO: Improve
        # Determines if the requested path is likely a package listing based on its format.         
        return path.endswith('/') or '.' not in os.path.basename(path) or path == '/'

class ProxyServer:
    def __init__(self, port=8001):
        self.port = port
        self.server = None
        self.thread = None
        self.url = f"http://localhost:{port}"

    def start(self, token, repo_url):
        ProxyHTTPRequestHandler.token = token
        ProxyHTTPRequestHandler.repo_url = repo_url
        self.server = HTTPServer(('', self.port), ProxyHTTPRequestHandler)
        self.thread = threading.Thread(target=self.server.serve_forever)
        self.thread.start()

    def stop(self):
        if self.server:
            self.server.shutdown()
            self.server.server_close()
            self.thread.join()