#!/usr/bin/python3

from argparse import ArgumentParser
from http.server import HTTPServer, BaseHTTPRequestHandler

class MyHTTPReqHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("{} wrote:".format(self.client_address[0]))
        self.wfile.write(b'ok\r\n')
        self.close_connection = True


ap = ArgumentParser()
ap.add_argument('-p', '--listen-port', type=int, default=51016,
                help='port to listen for email reads on')
args = ap.parse_args()


httpd = HTTPServer(('', args.listen_port), MyHTTPReqHandler)
httpd.serve_forever()
