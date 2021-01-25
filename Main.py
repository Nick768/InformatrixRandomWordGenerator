from pysrc.HTTPServer import HTTPServer

# enter your local IP to be able to connect other devices in the same network
serveraddress = "localhost"
port = 8080

# set this to False if you don't want to get debugging messages
# if it's set to True, your browser doesn't start up automatically!
isDevelopmentVersion = True

allowedRequestableFileExtensions = [
    ".js", ".css", ".png",
    ".svg", ".jpg", ".css",
    ".json", ".ico", ".xml"
]


if __name__ == "__main__":
    HTTPServer.startserver(HTTPServer.RequestHandler)
