from .PathManager import *

def getContentOfHTML():
    from .HTTPServer import requestedPath
    if requestedPath != "/" and requestedPath != "/newRound/":
        try:
            path = translate_path_for_html_loading("/websrc/" + requestedPath) + ".html"
            with open(path, "rb") as f:
                output = "".encode("UTF-8")
                lines = f.readlines()
                for line in lines:
                    output += line
                return output.decode()
        except:
            pass
    return ""

def showNewRoundButton():
    from .ListManager import getCurrentWord
    if "Kein weiteres Wort vorhanden!" == getCurrentWord():
        try:
            path = translate_path_for_html_loading("/websrc/newRound.html")
            with open(path, "rb") as f:
                output = "".encode("UTF-8")
                lines = f.readlines()
                for line in lines:
                    output += line
                return output.decode()
        except:
            pass
    return ""