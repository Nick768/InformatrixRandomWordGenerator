from pysrc.HTTPServer import HTTPServer

# enter your local IP to be able to connect other devices in the same network
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
    ".json",
    ".xml"
]

HTTPServer.startserver(HTTPServer)
