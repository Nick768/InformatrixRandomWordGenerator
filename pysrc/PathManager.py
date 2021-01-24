from urllib.parse import unquote
from posixpath import normpath
from os import curdir, pardir, getcwd
from os.path import dirname, join


def translate_path_for_html_loading(path):
    path = path.split('?', 1)[0]
    path = path.split('#', 1)[0]
    trailing_slash = path.rstrip().endswith('/')
    try:
        path = unquote(path, errors='surrogatepass')
    except UnicodeDecodeError:
        path = unquote(path)
    path = normpath(path)
    words = path.split('/')
    words = filter(None, words)
    path = getcwd()
    for word in words:
        if dirname(word) or word in (curdir, pardir):
            continue
        path = join(path, word)
    return path
