import sys
import os


def resource_path(relative_path):
    """
    Get absolute path to resource, works for dev and for PyInstaller
    https://thetopsites.net/article/51314351.shtml
    """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS

        if 'resource/' in relative_path:
            relative_path = relative_path.replace('resource/', '')
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
