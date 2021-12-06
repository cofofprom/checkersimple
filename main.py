import subprocess
import http.server

class Resp(http.server.BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/json')
        self.end_headers()

    def do_GET(self):
        self._set_response()
        self.wfile.write("{'hello!'}".encode("utf-8"))

server_address = ("", 8080)
h = http.server.HTTPServer(server_address, Resp)
h.serve_forever()


#subprocess.run("python D:\\projects\\govno.py", stdin=open("input.txt", "r"), stdout=open("result.txt", "w"))
