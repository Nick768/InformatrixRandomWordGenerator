from pysrc.HTTPServer import HTTPServer

# enter your local IP to be able to connect other devices in the same network
serveradress = "localhost"
port = 8080

allowedRequestableFileExtensions = [
    ".js", ".css", ".png",
    ".svg", ".jpg", ".css",
    ".json", ".ico", ".xml"
]


if __name__ == "__main__":
    HTTPServer.startserver(HTTPServer.RequestHandler)
