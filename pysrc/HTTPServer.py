from http.server import SimpleHTTPRequestHandler
from io import BytesIO
from os import fstat
from socketserver import TCPServer
from .ReplaceableValues import ReplaceableValues

requestedPath = str


class HTTPServer:

    class RequestHandler(SimpleHTTPRequestHandler):
        def do_GET(self):
            from Main import allowedFileExtensions

            global requestedPath
            requestedPath = self.path

            ##### Functions >> #####

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
                    if response == 404:
                        sendHeaderWithResponse(self, 404)
                        self.wfile.write(
                            "Housten, we have a problem!".encode("UTF-8"))
                    else:
                        self.path = "/websrc/404.html"
                        sendRequestedFile(self)

            def replaceHTMLVars(file_or_str):
                if type(file_or_str) == str:
                    file_or_str = BytesIO(file_or_str.encode("UTF-8"))

                flines = file_or_str.readlines()
                output = ""
                for line in flines:
                    outputLine = line
                    # only try to parse lines with two '%%'
                    if line.count("%%".encode("UTF-8")) == 2:
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
                                    replaceable = 'ERROR: "%s" is no callable function without arguments or not a primitive or does contain errors!' % variableToReplace
                            if replaceable.strip("\t ") == "\r\n" or replaceable.strip("\t ") == "\n" or replaceable.strip("\t ") == "\r" or replaceable.strip("\t ") == "":
                                outputLine = b""
                            else:
                                outputLine = line.replace(
                                    bytes("%%" + variableToReplace + "%%", "UTF-8"), bytes(replaceable, "UTF-8"))

                    output += outputLine.decode()
                if output.__contains__("%%"):
                    output = replaceHTMLVars(output)
                return output

            ##### << Functions #####

            if self.path.endswith("/") or self.path == "":
                self.path = "/websrc/main.html"

                try:
                    path = self.translate_path(self.path)
                    f = open(path, 'rb')
                    output = replaceHTMLVars(f)
                    sendHeaderWithResponse(self, 200)
                    self.wfile.write(bytes(output, "UTF-8"))
                    f.close()
                except:
                    self.path = "/websrc/404.html"
                    sendRequestedFile(self)

            else:
                requestAllowed = False
                for extension in allowedFileExtensions:
                    if self.path.endswith(extension):
                        requestAllowed = True
                        break

                if not requestAllowed:
                    self.path = "/websrc/404.html"
                sendRequestedFile(self)

    def startserver(RequestHandler):
        from Main import serveradress, port

        with TCPServer((serveradress, port), RequestHandler) as httpd:
            try:
                print("Server started: %s:%s" %
                      (serveradress, port))
                httpd.serve_forever()
            except KeyboardInterrupt:
                pass

            httpd.server_close()
            print("Server stopped")
