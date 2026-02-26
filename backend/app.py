from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write(b"Hello from Effective Mobile!")
        else:
            self.send_error(404, "Not Found")

if __name__ == '__main__':
    server_address = ('localhost', 8080)
    httpd = HTTPServer(server_address, SimpleHandler)
    # print("Server running on port 8080...")
    httpd.serve_forever()
