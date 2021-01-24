from pysrc.HTTPServer import HTTPServer

serveraddress = "127.0.0.1"
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
