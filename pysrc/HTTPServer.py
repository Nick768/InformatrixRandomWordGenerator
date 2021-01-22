from http.server import SimpleHTTPRequestHandler
from os import fstat
from socketserver import TCPServer
from .ReplaceableValues import ReplaceableValues


class HTTPServer:
    serveraddress = "127.0.0.1"
    port = 8080

    allowedFileExtensions = [
        ".js",
        ".css",
        ".png",
        ".svg",
        ".jpg",
        ".css",
        ".ico"
    ]

    class RequestHandler(SimpleHTTPRequestHandler):
        def do_GET(self):
            def sendHeaderWithResponse(self, response):
                self.send_response(response)
                self.send_header(
                    "Content-type", self.guess_type(self.translate_path(self.path)))
                try:
                    self.send_header("Content-Length", str(self.fs[6]))
                except:
                    pass
                self.end_headers()

            def sendRequestedFile(self):
                if self.path == "/websrc/404.html":
                    response = 404
                else:
                    response = 200
                try:
                    path = self.translate_path(self.path)
                    f = open(path, 'rb')
                    self.fs = fstat(f.fileno())
                    sendHeaderWithResponse(self, response)
                    self.copyfile(f, self.wfile)
                    f.close()
                except:
                    sendHeaderWithResponse(self, 404)
                    self.wfile.write("oh... big problem!".encode("UTF-8"))

            if self.path.endswith("/") or self.path == "":
                while self.path.endswith("/"):
                    self.path = self.path[0:-1]

                if self.path == "/" or self.path == "":
                    self.path = "/websrc/main.html"
                else:
                    self.path = "/websrc" + self.path + ".html"

                try:
                    path = self.translate_path(self.path)
                    f = open(path, 'rb')
                    flines = f.readlines()

                    output = ""
                    for line in flines:
                        outputLine = line
                        if line.count("%%".encode("UTF-8")) == 2: # only try to parse lines with two '%%'
                            start = line.index("%%".encode("UTF-8")) + 2
                            stop = line.index("%%".encode("UTF-8"), start)
                            variableToReplace = line.replace(
                                line[stop:-1], b"").replace(line[0:start], b"").decode().strip()

                            if hasattr(ReplaceableValues, variableToReplace):
                                replaceable = getattr(
                                    ReplaceableValues, variableToReplace)
                                if str(type(replaceable)) == "<class 'function'>":
                                    try:
                                        replaceable = replaceable()
                                    except:
                                        replaceable = 'ERROR: "%s" is no callable function without arguments or not a primitive!' % variableToReplace
                                outputLine = line.replace(
                                    bytes("%%" + variableToReplace + "%%", "UTF-8"), bytes(replaceable, "UTF-8"))

                        output += outputLine.decode()
                    sendHeaderWithResponse(self, 200)
                    self.wfile.write(bytes(output, "UTF-8"))
                    f.close()
                except:
                    self.path = "/websrc/404.html"
                    sendRequestedFile(self)

            else:
                requestAllowed = False
                for extension in HTTPServer.allowedFileExtensions:
                    if self.path.__contains__(extension):
                        requestAllowed = True

                if not requestAllowed:
                    self.path = "/websrc/404.html"
                sendRequestedFile(self)

    def startserver(self):
        with TCPServer((self.serveraddress, self.port), self.RequestHandler) as httpd:
            try:
                print("Server started: %s:%s" %
                      (self.serveraddress, self.port))
                httpd.serve_forever()
            except KeyboardInterrupt:
                pass

            httpd.server_close()
            print("Server stopped")
