import wx

from bitmap_panel import BitmapPanel
from blrevive_enums import UIAttachment
from blrevive_toolkit import get_parent_frame
from blrevive_gear import BLReviveReceiver, BLReviveStock, BLReviveBarrel, BLReviveScope, BLReviveMuzzle, BLReviveMagazine, BLReviveGrip, BLReviveTag, BLReviveCamo
from helpers_pyinstaller import resource_path


class PartSelectPanel(BitmapPanel):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        self.DisableBitmap(True)

        self.PartID = UIAttachment.NONE

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

        self.Bind(wx.EVT_LEFT_UP, self.ui_panel_OnLeftUp)
        self.ui_toggle.Bind(wx.EVT_TOGGLEBUTTON, self.ui_toggle_OnToggleButton)
        self.ui_bitmap.Bind(wx.EVT_LEFT_UP, self.ui_bitmap_OnLeftUp)
        self.ui_text.Bind(wx.EVT_LEFT_UP, self.ui_text_OnLeftUp)
        self.ui_reset.Bind(wx.EVT_BUTTON, self.ui_reset_OnButtonClick)

    def set_part_elements(self, part_id, toggle_img, text_font, text_label, image_bmp, reset_bmp):
        if type(part_id) == UIAttachment:
            self.PartID = part_id
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

    def set_part(self, part_id):
        text_label = None
        image_bmp = None
        font_blr_UI_12 = wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "ProFontWindows")
        reset_bmp = wx.Image.ConvertToBitmap(wx.Image(resource_path('resource/FoxGame/Content/Packages/UI2/Menu/t_exitgame.TGA')))

        if part_id == UIAttachment.MUZZLE:
            toggle_img = wx.Image(resource_path('resource/FoxGame/Content/Packages/UI2/Menu/Muzzle.TGA'))
            text_font = font_blr_UI_12

        elif part_id == UIAttachment.GRIP:
            toggle_img = wx.Image(resource_path('resource/FoxGame/Content/Packages/UI2/Menu/Grip.TGA'))
            text_font = font_blr_UI_12

        elif part_id == UIAttachment.BARREL:
            toggle_img = wx.Image(resource_path('resource/FoxGame/Content/Packages/UI2/Menu/Barrel.TGA'))
            text_font = font_blr_UI_12

        elif part_id == UIAttachment.MAGAZINE:
            toggle_img = wx.Image(resource_path('resource/FoxGame/Content/Packages/UI2/Menu/Mag.TGA'))
            text_font = font_blr_UI_12

        elif part_id == UIAttachment.SCOPE:
            toggle_img = wx.Image(resource_path('resource/FoxGame/Content/Packages/UI2/Menu/Scope.TGA'))
            text_font = font_blr_UI_12

        elif part_id == UIAttachment.STOCK:
            toggle_img = wx.Image(resource_path('resource/FoxGame/Content/Packages/UI2/Menu/Stock.TGA'))
            text_font = font_blr_UI_12

        elif part_id == UIAttachment.TAG:
            toggle_img = wx.Image(resource_path('resource/FoxGame/Content/Packages/UI2/Menu/Tag.TGA'))
            text_font = font_blr_UI_12

        elif part_id == UIAttachment.CAMO:
            toggle_img = wx.Image(resource_path('resource/FoxGame/Content/Packages/UI2/Menu/Camo.TGA'))
            text_font = font_blr_UI_12

        elif part_id == UIAttachment.RECEIVER:
            toggle_img = wx.Image(resource_path('resource/FoxGame/Content/Packages/UI2/Menu/reciever.TGA'))
            text_font = font_blr_UI_12
            reset_bmp = wx.Image.ConvertToBitmap(wx.Image(resource_path('resource/FoxGame/Content/Packages/UI2/Menu/t_viewLast.TGA')).Resize(wx.Size(30, 34), wx.DefaultPosition))

        self.set_part_elements(part_id, toggle_img, text_font, text_label, image_bmp, reset_bmp)

    def create_attachment(self, name, fname, bitmap_path, icon_path):
        if self.PartID == UIAttachment.RECEIVER:
            return BLReviveReceiver(name, fname, bitmap_path, icon_path)

        if self.PartID == UIAttachment.MUZZLE:
            return BLReviveMuzzle(name, fname, bitmap_path, icon_path)

        if self.PartID == UIAttachment.GRIP:
            return BLReviveGrip(name, fname, bitmap_path, icon_path)

        if self.PartID == UIAttachment.BARREL:
            return BLReviveBarrel(name, fname, bitmap_path, icon_path)

        if self.PartID == UIAttachment.MAGAZINE:
            return BLReviveMagazine(name, fname, bitmap_path, icon_path)

        if self.PartID == UIAttachment.SCOPE:
            return BLReviveScope(name, fname, bitmap_path, icon_path)

        if self.PartID == UIAttachment.STOCK:
            return BLReviveStock(name, fname, bitmap_path, icon_path)

        if self.PartID == UIAttachment.TAG:
            return BLReviveTag(name, fname, bitmap_path, icon_path)

        if self.PartID == UIAttachment.CAMO:
            return BLReviveCamo(name, fname, bitmap_path, icon_path)

    def reset_attachment(self):
        self.ui_text.SetLabel('')
        self.ui_bitmap.SetBitmap(wx.NullBitmap)

    def handle_reset_attachment(self):
        parentframe = get_parent_frame(self)

        if self.PartID != UIAttachment.RECEIVER:
            self.reset_attachment()
        else:
            for psp in parentframe.part_select_panels[1:]:
                psp.reset_attachment()

        parentframe.export_current_loadouts()

    def handle_ui_panel_selected(self):
        self.ui_toggle.SetValue(True)
        if self.ui_toggle.GetValue():
            get_parent_frame(self).handle_gear_toggle(self.PartID)
        else:
            self.ui_toggle.SetValue(True)

    def ui_panel_OnLeftUp(self, event):
        self.handle_ui_panel_selected()

    def ui_toggle_OnToggleButton(self, event):
        self.handle_ui_panel_selected()

    def ui_bitmap_OnLeftUp(self, event):
        self.handle_ui_panel_selected()

    def ui_text_OnLeftUp(self, event):
        self.handle_ui_panel_selected()

    def ui_reset_OnButtonClick(self, event):
        self.handle_reset_attachment()
