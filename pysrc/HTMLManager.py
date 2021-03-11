from .PathManager import *


def loadFile(path):
    try:
        with open(path, "rb") as f:
            output = "".encode("UTF-8")
            lines = f.readlines()
            for line in lines:
                output += line
            return output.decode()
    except FileNotFoundError:
        return 404


def getContentOfHTML():
    from .HTTPServer import requestedPath
    if requestedPath != "/" and requestedPath != "/newRound/":
        path = translate_path_for_loading(
            "/websrc/" + requestedPath) + ".html"
        return loadFile(path)
    return ""


def showNewRoundButton():
    from .ListManager import getCurrentWord
    if "Kein weiteres Wort vorhanden!" == getCurrentWord():
        path = translate_path_for_loading("/websrc/newRound.html")
        return loadFile(path)
    return ""
