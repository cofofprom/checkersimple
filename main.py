import subprocess
import http.server
import os

class Resp(http.server.BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/json')
        self.end_headers()

    def do_GET(self):
        self._set_response()
        self.wfile.write("{'hello!'}".encode("utf-8"))
        
    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        pfile = open("tt.py", "w")
        pfile.write(post_data)
        outfile = open("result.txt", "w")
        #outfile.close()
        subprocess.run("python3 tt.py", stdout=outfile)
        pfile.close()
        outfile.close()
        infile = open("result.txt", "r")
        self.wfile.write(infile.read(1024))
        infile.close()
        
server_address = ("", int(os.environ["PORT"]))
print(server_address)
h = http.server.HTTPServer(server_address, Resp)
h.serve_forever()


#subprocess.run("python D:\\projects\\govno.py", stdin=open("input.txt", "r"), stdout=open("result.txt", "w"))
