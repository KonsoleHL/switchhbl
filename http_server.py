#!/usr/bin/python2

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
import random

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        if self.path == '/':
            self.path = '/index.html'

        if '?' in self.path:
            self.path = self.path[:self.path.find('?')]

        f = open('build' + self.path, "r")
        self.wfile.write(f.read())

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        self._set_headers()
        print "in post method"
        self.data_string = self.rfile.read(int(self.headers['Content-Length']))

        self.send_response(200)
        self.end_headers()

        print self.data_string

class ThreadedHTTPServer(SocketServer.ThreadingMixIn, HTTPServer):
    pass


def run(server_class=ThreadedHTTPServer, handler_class=S, port=80):
    server_address = ('192.168.2.200', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

if len(argv) == 2:
    run(port=int(argv[1]))
else:
    run()
