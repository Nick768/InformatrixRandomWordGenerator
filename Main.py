from pysrc.HTTPServer import HTTPServer

serveradress = "localhost"
port = 8080

allowedFileExtensions = [
    ".js",
    ".css",
    ".png",
    ".svg",
    ".jpg",
    ".css",
    ".ico",
    ".json"
]

HTTPServer.startserver(HTTPServer)
