# -*- coding: utf-8 -*-
"""
PyInstaller Helpers | Methods to make life with PyInstaller less painful.

Version 1.0
Requires: N/A

@author: Kinetos#6935
"""
import sys
import os


def resource_path(relative_path):
    """
    Get absolute path to resource for pyinstaller redirects
    Based on code from: https://thetopsites.net/article/51314351.shtml
    """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS

        if 'resource/' in relative_path:
            relative_path = relative_path.replace('resource/', '')
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
