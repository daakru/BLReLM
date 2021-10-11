# -*- coding: utf-8 -*-
"""
BitmapPanel | Adds a bitmap as the background on a wxPanel.

Version 1.0
Requires: wxPython, resource_path.py (v1.0)

@author: Kinetos#6935
"""
import wx
from helpers_pyinstaller import resource_path


# --------------------------------------------------------------------------- #


class BitmapPanel(wx.Panel):
    """
    Panel with bitmap as the background heavily based on code from the following source:
    https://www.blog.pythonlibrary.org/2010/03/18/wxpython-putting-a-background-image-on-a-panel/
    """

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        image_file = resource_path('resource/images/BLReLM_wall.png')
        # self.bitmap = wx.Image(image_file, wx.BITMAP_TYPE_ANY).Scale(1280, 720).ConvertToBitmap()
        self.bitmap = wx.Image(image_file, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bitmap_pos = wx.DefaultPosition
        self.bitmap_size = wx.DefaultSize
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)

# --------------------------------------------------------------------------- #

    def OnEraseBackground(self, event):
        dc = event.GetDC()

        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        bmp = self.bitmap
        dc.DrawBitmap(bmp, self.bitmap_pos.x, self.bitmap_pos.y)

# --------------------------------------------------------------------------- #

    def SetPanelBitmap(self, bitmap_path):
        self.bitmap = wx.Image(bitmap_path, wx.BITMAP_TYPE_ANY).ConvertToBitmap()

# --------------------------------------------------------------------------- #

    def SetPanelBitmapPosition(self, pos):
        self.bitmap_pos = pos

# --------------------------------------------------------------------------- #

    def SetPanelBitmapSize(self, size):
        self.bitmap_size = size

# --------------------------------------------------------------------------- #

    def SetPanelBitmapPositionToParent(self):
        parent_pos = self.GetParent().GetScreenPosition()
        # sizer = self.GetContainingSizer()
        screen_pos = self.GetScreenPosition()
        offset = parent_pos - screen_pos
        offset = offset.Get()
        neg_point = wx.Point(offset[0], offset[1])
        self.SetPanelBitmapPosition(neg_point)

# --------------------------------------------------------------------------- #

    def GetPanelBitmap(self):
        return self.bitmap

# --------------------------------------------------------------------------- #
