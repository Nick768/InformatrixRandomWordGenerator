from pysrc.HTTPServer import HTTPServer
from platform import system as osname

# enter your local IP to be able to connect other devices in the same network
serveraddress = "localhost"
port = 8080

# if it's set to True, your browser doesn't start up automatically!
isDevelopmentVersion = True

allowedRequestableFileExtensions = [
    ".js", ".css", ".png",
    ".svg", ".jpg", ".css",
    ".json", ".ico", ".xml"
]


if __name__ == "__main__":
    if not isDevelopmentVersion:
        try:
            from os import system  # yes, I could use the webbrowser library
                                   # but on Windows it opens up IE or Edge :(
            if osname() == "Linux":
                system('xdg-open http://%s:%s &> /dev/null' %
                       (serveraddress, port))
            elif osname() == "Darwin":
                system('open http://%s:%s' % (serveraddress, port))
            elif osname() == "Windows":
                system('start "" http://%s:%s' % (serveraddress, port))
            else:
                print("Can't open your browser automatically.")
                print("Your OS isn't supported!")
        except:
            print("Can't open your browser automatically.")
            print("Maybe your OS isn't supported or you don't have a browser!")

    HTTPServer.startserver(HTTPServer.RequestHandler)
