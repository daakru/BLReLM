import wx

from bitmap_panel import BitmapPanel


class PartSelectPanel(BitmapPanel):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        self.DisableBitmap(True)

        # self.SetBorder(wx.BORDER_SIMPLE)
        # self.SetPosition(wx.DefaultPosition)
        # self.SetSize(wx.DefaultSize)
        self.SetBackgroundColour(wx.Colour(0, 64, 128))

        bSizerPSP = wx.BoxSizer(wx.HORIZONTAL)

        self.ui_toggle = wx.BitmapToggleButton(self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size(32, 32), wx.BORDER_NONE)
        # self.ui_toggle.SetValue(True)

        self.ui_toggle.SetBitmap(wx.NullBitmap)
        self.ui_toggle.SetBackgroundColour(wx.Colour(48, 48, 48))

        bSizerPSP.Add(self.ui_toggle, 0, wx.ALL, 0)

        self.ui_bitmap = wx.StaticBitmap(self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0)
        self.ui_bitmap.SetMinSize(wx.Size(64, 32))
        self.ui_bitmap.SetMaxSize(wx.Size(64, 32))

        bSizerPSP.Add(self.ui_bitmap, 0, wx.LEFT | wx.RIGHT, 8)

        self.ui_text = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.ui_text.Wrap(-1)

        self.ui_text.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        bSizerPSP.Add(self.ui_text, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 0)

        self.ui_reset = wx.BitmapButton(self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size(32, 32), wx.BU_AUTODRAW | 0 | wx.BORDER_NONE)

        self.ui_reset.SetBitmapPosition(wx.BOTTOM)
        self.ui_reset.SetBackgroundColour(wx.Colour(0, 64, 128))

        bSizerPSP.Add(self.ui_reset, 0, wx.ALL, 0)

        self.SetSizer(bSizerPSP)
        self.Layout()
        bSizerPSP.Fit(self)
        # parentSizer.Add( self, 0, wx.EXPAND |wx.ALL, 4 )

    def set_part_elements(self, toggle_img, text_font, text_label, image_bmp, reset_bmp):
        if toggle_img is not None:
            toggle_img = toggle_img.Scale(32, 32)
            self.ui_toggle.SetBitmap(wx.Image.ConvertToBitmap(toggle_img))
            toggle_img.Replace(255, 255, 255, 255, 165, 0)
            self.ui_toggle.SetBitmapPressed(wx.Image.ConvertToBitmap(toggle_img))
        if text_font is not None:
            self.ui_text.SetFont(text_font)
        if text_label is not None:
            self.ui_text.SetLabel(text_label)
        if image_bmp is not None:
            self.ui_bitmap.SetBitmap(image_bmp)
        if reset_bmp is not None:
            self.ui_reset.SetBitmap(reset_bmp)
