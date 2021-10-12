# -*- coding: utf-8 -*-
"""
BLRevive Loadout Manager | Loadout Generation UI for MagiCow's Server.

Version 1.0.1
Requires: wxPython, __WXFB_BLR_LMGR.py (vN/A),
          blrevive_toolkit.py (v1.0), wso.py (v1.3.0)
          helpers_pyinstaller.py (v1.0), blrevive_gear.py (v1.0)

@author: Kinetos#6935
"""
import wx
from pandas.io.clipboard import copy
import wso as wsobj
import blrevive_toolkit as blrtk
from __WXFB_BLR_LMGR import BLR_LMGR_FRAME
from helpers_pyinstaller import resource_path
from blrevive_gear import BLReviveLoadout, BLReviveWeapon, BLReviveReceiver, BLReviveStock, BLReviveBarrel, BLReviveScope


try:
    import pyi_splash
except Exception:
    pass

# --------------------------------------------------------------------------- #


def __build_parser():
    p = wsobj.generate_outfile_parser(description=__doc__.split("@author:")[0])
    p.add_argument("-d", "--debug", dest="debug", action="store_true",
                   help="enable debug print statements.")
    return p


# --------------------------------------------------------------------------- #


class BLRFrame(BLR_LMGR_FRAME):
    def __init__(self, parent, logfile=None, debug=False):
        super().__init__(parent)

        # Create our writable string object
        self.ln = wsobj.init('{0}', o=logfile, d=debug)

        # Load user settings from settings.json
        self.user_settings = blrtk.get_user_config()

        self.loadouts = {}
        self.active_loadout = 'm_bmToggleBtnPrimary1'
        self.m_bmToggleBtnPrimary1.SetValue(True)

        # Add fonts
        wx.Font.AddPrivateFont(resource_path('resource/fonts/ProFontWindows/ProFontWindows.ttf'))
        self.font_blr_UI = wx.Font(-1, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "ProFontWindows")
        self.font_blr_UI_12 = wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "ProFontWindows")
        self.font_blr_UI_14 = wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "ProFontWindows")
        self.font_blr_UI_16 = wx.Font(16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "ProFontWindows")
        self.font_blr_UI_24 = wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "ProFontWindows")
        self.font_blr_UI_32 = wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "ProFontWindows")

        # Set up columns in the List Control
        self.receiver_columns = ['Receiver', 'Damage', 'Firerate', 'Ammo', 'Reload', 'Zoom', 'ScopeIn', 'Spread-Aim', 'Spread-Hip', 'Recoil', 'Range', 'Run']

        self.stock_columns = self.receiver_columns.copy()
        self.stock_columns[0] = 'Stock'

        self.barrel_columns = self.receiver_columns.copy()
        self.barrel_columns[0] = 'Barrel'

        self.scope_columns = self.receiver_columns.copy()
        self.scope_columns[0] = 'Scope'

        # Lazy mode for now to get exporting to MagiCow functional
        self.temp_receivers = blrtk.get_receivers()
        self.temp_stocks = blrtk.get_stocks()
        self.temp_barrels = blrtk.get_barrels()
        self.temp_scopes = blrtk.get_scopes()

        self.df_primary = blrtk.build_receivers_dataframe()

# --------------------------------------------------------------------------- #

        # Scintilla
        # print(f'Lexer: {self.m_scintilla1.GetLexer()}')
        self.m_scintilla1.StyleSetFont(0, self.font_blr_UI)
        self.m_scintilla1.SetUseHorizontalScrollBar(False)
        self.m_scintilla1.SetLexer(wx.stc.STC_LEX_CONF)
        # self.m_scintilla1.SetVScrollBar() SetMouseWheelCaptures SetMouseDownCaptures

        # List Control
        headerattr = wx.ItemAttr()
        headerattr.SetFont(self.font_blr_UI_14)
        self.m_listCtrl_blrlm_selector.SetHeaderAttr(headerattr)
        self.m_bitmap_blrlm_preview.SetBackgroundColour(wx.Colour(0, 64, 128))

        # Bitmap Panels
        self.m_panel_blrlm_preview.SetPanelBitmapPositionToParent()
        self.m_panel_partselect.SetPanelBitmapPositionToParent()
        self.m_panel11.SetPanelBitmapPositionToParent()

        # Toggle Buttons
        image = wx.Image(resource_path('resource/FoxGame/Content/Packages/UI2/Menu/reciever.TGA')).Scale(32, 32)
        self.m_bmToggleBtn_blrlm_receiver.SetBitmap(wx.Image.ConvertToBitmap(image))
        image.Replace(255, 255, 255, 255, 165, 0)
        self.m_bmToggleBtn_blrlm_receiver.SetBitmapPressed(wx.Image.ConvertToBitmap(image))

        image = wx.Image(resource_path('resource/FoxGame/Content/Packages/UI2/Menu/Stock.TGA')).Scale(32, 32)
        self.m_bmToggleBtn_blrlm_stock.SetBitmap(wx.Image.ConvertToBitmap(image))
        image.Replace(255, 255, 255, 255, 165, 0)
        self.m_bmToggleBtn_blrlm_stock.SetBitmapPressed(wx.Image.ConvertToBitmap(image))

        image = wx.Image(resource_path('resource/FoxGame/Content/Packages/UI2/Menu/Barrel.TGA')).Scale(32, 32)
        self.m_bmToggleBtn_blrlm_barrel.SetBitmap(wx.Image.ConvertToBitmap(image))
        image.Replace(255, 255, 255, 255, 165, 0)
        self.m_bmToggleBtn_blrlm_barrel.SetBitmapPressed(wx.Image.ConvertToBitmap(image))

        image = wx.Image(resource_path('resource/FoxGame/Content/Packages/UI2/Menu/Scope.TGA')).Scale(32, 32)
        self.m_bmToggleBtn_blrlm_scope.SetBitmap(wx.Image.ConvertToBitmap(image))
        image.Replace(255, 255, 255, 255, 165, 0)
        self.m_bmToggleBtn_blrlm_scope.SetBitmapPressed(wx.Image.ConvertToBitmap(image))

        # Loadout Toggle Buttons
        image = wx.Image(resource_path('resource/FoxGame/Content/Packages/UI2/UI_Icons/Gear/t_AR.TGA')).Scale(64, 64)
        self.m_bmToggleBtnPrimary1.SetBitmap(wx.Image.ConvertToBitmap(image))
        image.Replace(255, 255, 255, 255, 165, 0)
        self.m_bmToggleBtnPrimary1.SetBitmapPressed(wx.Image.ConvertToBitmap(image))

        image = wx.Image(resource_path('resource/FoxGame/Content/Packages/UI2/UI_Icons/Gear/t_smg.TGA')).Scale(64, 64)
        self.m_bmToggleBtnPrimary2.SetBitmap(wx.Image.ConvertToBitmap(image))
        image.Replace(255, 255, 255, 255, 165, 0)
        self.m_bmToggleBtnPrimary2.SetBitmapPressed(wx.Image.ConvertToBitmap(image))

        image = wx.Image(resource_path('resource/FoxGame/Content/Packages/UI2/UI_Icons/Gear/t_bolt01.TGA')).Scale(64, 64)
        self.m_bmToggleBtnPrimary3.SetBitmap(wx.Image.ConvertToBitmap(image))
        image.Replace(255, 255, 255, 255, 165, 0)
        self.m_bmToggleBtnPrimary3.SetBitmapPressed(wx.Image.ConvertToBitmap(image))

        image = wx.Image(resource_path('resource/FoxGame/Content/Packages/UI2/UI_Icons/Gear/t_9mm.TGA')).Scale(64, 64)
        self.m_bmToggleBtnSecondary1.SetBitmap(wx.Image.ConvertToBitmap(image))
        image.Replace(255, 255, 255, 255, 165, 0)
        self.m_bmToggleBtnSecondary1.SetBitmapPressed(wx.Image.ConvertToBitmap(image))

        image = wx.Image(resource_path('resource/FoxGame/Content/Packages/UI2/UI_Icons/Gear/t_revolver.TGA')).Scale(64, 64)
        self.m_bmToggleBtnSecondary2.SetBitmap(wx.Image.ConvertToBitmap(image))
        image.Replace(255, 255, 255, 255, 165, 0)
        self.m_bmToggleBtnSecondary2.SetBitmapPressed(wx.Image.ConvertToBitmap(image))

        image = wx.Image(resource_path('resource/FoxGame/Content/Packages/UI2/UI_Icons/Gear/t_machpistol01.TGA')).Scale(64, 64)
        self.m_bmToggleBtnSecondary3.SetBitmap(wx.Image.ConvertToBitmap(image))
        image.Replace(255, 255, 255, 255, 165, 0)
        self.m_bmToggleBtnSecondary3.SetBitmapPressed(wx.Image.ConvertToBitmap(image))

        # image = wx.Image(resource_path('resource/FoxGame/Content/Packages/UI2/UI_Emblems/Top/t_emblem_top_62.TGA')).Scale(24, 24)
        # self.m_bmToggleBtnLoadout1.SetBitmap(wx.Image.ConvertToBitmap(image))
        # image.Replace(255, 255, 255, 255, 165, 0)
        # self.m_bmToggleBtnLoadout1.SetBitmapPressed(wx.Image.ConvertToBitmap(image))
        self.m_bmToggleBtnLoadout1.SetLabelMarkup('<span face="ProFontWindows" size="14336">LOADOUT 1</span>')

        # image = wx.Image(resource_path('resource/FoxGame/Content/Packages/UI2/UI_Emblems/Top/t_emblem_top_63.TGA')).Scale(24, 24)
        # self.m_bmToggleBtnLoadout2.SetBitmap(wx.Image.ConvertToBitmap(image))
        # image.Replace(255, 255, 255, 255, 165, 0)
        # self.m_bmToggleBtnLoadout2.SetBitmapPressed(wx.Image.ConvertToBitmap(image))
        self.m_bmToggleBtnLoadout2.SetLabelMarkup('<span face="ProFontWindows" size="14336">LOADOUT 2</span>')

        # image = wx.Image(resource_path('resource/FoxGame/Content/Packages/UI2/UI_Emblems/Top/t_emblem_top_64.TGA')).Scale(24, 24)
        # self.m_bmToggleBtnLoadout3.SetBitmap(wx.NullBitmap)  # wx.Image.ConvertToBitmap(image)
        # image.Replace(255, 255, 255, 255, 165, 0)
        # self.m_bmToggleBtnLoadout3.SetBitmapPressed(wx.NullBitmap)  # (wx.Image.ConvertToBitmap(image))
        self.m_bmToggleBtnLoadout3.SetLabelMarkup('<span face="ProFontWindows" size="14336">LOADOUT 3</span>')

        # Toggle Text
        self.m_staticText_blrlm_receiver.SetFont(self.font_blr_UI_12)
        self.m_staticText_blrlm_stock.SetFont(self.font_blr_UI_12)
        self.m_staticText_blrlm_barrel.SetFont(self.font_blr_UI_12)
        self.m_staticText_blrlm_scope.SetFont(self.font_blr_UI_12)

        def ListCompareFunction(item1, item2):
            item1 = str(item1)
            item2 = str(item2)
            item1 = self.df_primary.query('unlockid == @item1')['FriendlyName'][0]
            item2 = self.df_primary.query('unlockid == @item2')['FriendlyName'][0]
            if item1.upper() < item2.upper():
                return -1
            elif item1.upper() == item2.upper():
                return 0
            return 1

        self.m_listCtrl_blrlm_selector.SortItems(ListCompareFunction)

# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #

    def listctrl_load_columns(self, columns, upper=True):
        for col in columns:
            if upper:
                col = col.upper()
            self.m_listCtrl_blrlm_selector.AppendColumn(col)

# --------------------------------------------------------------------------- #

    def listctrl_clear_columns(self):
        self.m_listCtrl_blrlm_selector.DeleteAllColumns()

# --------------------------------------------------------------------------- #

    def listctrl_clear_rows(self):
        self.m_listCtrl_blrlm_selector.DeleteAllItems()

# --------------------------------------------------------------------------- #

    def listctrl_format_items(self):
        # Update Font
        for row in range(self.m_listCtrl_blrlm_selector.GetItemCount()):
            self.m_listCtrl_blrlm_selector.SetItemFont(row, self.font_blr_UI_12)
        # Sort by first column values
        for col in range(self.m_listCtrl_blrlm_selector.GetColumnCount()):
            self.m_listCtrl_blrlm_selector.SetColumnWidth(col, -2)
            width = self.m_listCtrl_blrlm_selector.GetColumnWidth(col)
            self.m_listCtrl_blrlm_selector.SetColumnWidth(col, -1)
            if width > self.m_listCtrl_blrlm_selector.GetColumnWidth(col):
                self.m_listCtrl_blrlm_selector.SetColumnWidth(col, -2)

# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #

    def listctrl_load_receivers(self):
        # Freeze the display of the control
        self.m_listCtrl_blrlm_selector.Freeze()

        # Clear the existing items
        self.listctrl_clear_rows()

        # Clear the existing columns
        self.listctrl_clear_columns()

        # Populate the columns for the Receivers
        self.listctrl_load_columns(self.receiver_columns)

        # Load Items
        for item in self.temp_receivers:
            self.m_listCtrl_blrlm_selector.Append([item])

        # column_ref = {}
        # i = 0
        # for col in self.df_primary.columns:
        #     column_ref[col] = i
        #     i += 1

        # def get_tuple_value(row, column_name):
        #     # Add 1 because the tuples returned by itertuples start with the index
        #     return row[column_ref[column_name] + 1]

        # def is_primary(row):
        #     return get_tuple_value(row, 'shortname').strip('"')[:3] == 'pri'

        # # Add Primary Weapons to the List Control
        # for row in self.df_primary.itertuples(name=None):
        #     if is_primary(row):  # row[16] == 'pri':
        #         self.m_listCtrl_blrlm_selector.Append([
        #             get_tuple_value(row, 'FriendlyName'),
        #             get_tuple_value(row, 'instanthitdamage[0]'),
        #             get_tuple_value(row, 'rateoffire'),
        #             get_tuple_value(row, 'magsize'),
        #             ' | '.join([a.strip().split('=')[-1] for a in str(get_tuple_value(row, 'reloadraterange')).strip('()').split(',')]),
        #             get_tuple_value(row, 'Sco'),
        #             get_tuple_value(row, 'weapontightaimtime'),
        #             get_tuple_value(row, 'basespread[0]'),
        #             round(float(get_tuple_value(row, 'basespread[0]')) * float(get_tuple_value(row, 'spreadzoommultiplier')), 4),
        #             get_tuple_value(row, 'recoilsize'),
        #             get_tuple_value(row, 'idealrange'),
        #             'weight: ' + str(get_tuple_value(row, 'weight'))
        #         ])
        #         self.m_listCtrl_blrlm_selector.SetItemData(self.m_listCtrl_blrlm_selector.GetItemCount() - 1, int(get_tuple_value(row, 'unlockid')))

        # Format the items
        self.listctrl_format_items()

        # Thaw the display of the control
        self.m_listCtrl_blrlm_selector.Thaw()

# --------------------------------------------------------------------------- #

    def listctrl_load_stocks(self):
        # Freeze the display of the control
        self.m_listCtrl_blrlm_selector.Freeze()

        # Clear the existing items
        self.listctrl_clear_rows()

        # Clear the existing columns
        self.listctrl_clear_columns()

        # Populate the columns for the Stocks
        self.listctrl_load_columns(self.stock_columns)

        # Load Items
        for item in self.temp_stocks:
            self.m_listCtrl_blrlm_selector.Append([item])

        # Format the items
        self.listctrl_format_items()

        # Thaw the display of the control
        self.m_listCtrl_blrlm_selector.Thaw()

# --------------------------------------------------------------------------- #

    def listctrl_load_barrels(self):
        # Freeze the display of the control
        self.m_listCtrl_blrlm_selector.Freeze()

        # Clear the existing items
        self.listctrl_clear_rows()

        # Clear the existing columns
        self.listctrl_clear_columns()

        # Populate the columns for the Barrels
        self.listctrl_load_columns(self.barrel_columns)

        # Load Items
        for item in self.temp_barrels:
            self.m_listCtrl_blrlm_selector.Append([item])

        # Format the items
        self.listctrl_format_items()

        # Thaw the display of the control
        self.m_listCtrl_blrlm_selector.Thaw()

# --------------------------------------------------------------------------- #

    def listctrl_load_scopes(self):
        # Freeze the display of the control
        self.m_listCtrl_blrlm_selector.Freeze()

        # Clear the existing items
        self.listctrl_clear_rows()

        # Clear the existing columns
        self.listctrl_clear_columns()

        # Populate the columns for the Scopes
        self.listctrl_load_columns(self.scope_columns)

        # Load Items
        for item in self.temp_scopes:
            self.m_listCtrl_blrlm_selector.Append([item])

        # Format the items
        self.listctrl_format_items()

        # Thaw the display of the control
        self.m_listCtrl_blrlm_selector.Thaw()

# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #

    def post_init(self):
        self.listctrl_load_receivers()

# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #

    def set_equipped_gear(self, event):
        # print('SET EQUIPPED GEAR')
        fname = event.GetText()
        ui_path = 'resource/FoxGame/Content/Packages/UI2/'
        bitmap_path = self.df_primary.query('FriendlyName == @fname')
        if not bitmap_path.empty:
            bitmap_path = bitmap_path.iloc[0].ImageIconRef
            bitmap_path = bitmap_path.replace('.', '/') + '.TGA'
            self.ln.dbwp(bitmap_path)
            image = wx.Image(resource_path(ui_path + bitmap_path))
            if image.GetWidth() == image.GetHeight():
                image = image.Scale(32, 32)
            else:
                image = image.Scale(64, 32)
            bitmap = wx.Image.ConvertToBitmap(image)
        else:
            bitmap = wx.NullBitmap  # wx.Bitmap()

        if self.m_bmToggleBtn_blrlm_receiver.GetValue():
            self.m_staticText_blrlm_receiver.SetLabel(fname)
            self.m_bitmap_blrlm_receiver.SetBitmap(bitmap)

        elif self.m_bmToggleBtn_blrlm_stock.GetValue():
            self.m_staticText_blrlm_stock.SetLabel(fname)
            self.m_bitmap_blrlm_stock.SetBitmap(bitmap)

        elif self.m_bmToggleBtn_blrlm_barrel.GetValue():
            self.m_staticText_blrlm_barrel.SetLabel(fname)
            self.m_bitmap_blrlm_barrel.SetBitmap(bitmap)

        elif self.m_bmToggleBtn_blrlm_scope.GetValue():
            self.m_staticText_blrlm_scope.SetLabel(fname)
            self.m_bitmap_blrlm_scope.SetBitmap(bitmap)

        self.export_current_loadouts()

# --------------------------------------------------------------------------- #

    def update_main_preview_image(self, bitmap):
        self.m_bitmap_blrlm_preview.SetBitmap(bitmap)

# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #

    def create_blrevive_weapon(self, name=None):
        # config_name, friendly_name, image_icon_path=None, small_icon_path=None, gear_types=[]
        fname = self.m_staticText_blrlm_receiver.GetLabelText()
        rec = self.df_primary.query('FriendlyName == @fname')
        if not rec.empty:
            name = rec.iloc[0].WPN
            bitmap_path = (rec.iloc[0].ImageIconRef).replace('.', '/') + '.TGA'
            small_bitmap = (rec.iloc[0].ImageIconRef).replace('.', '/') + '.TGA'
        else:
            name = None
            bitmap_path = None
            small_bitmap = None
        receiver = BLReviveReceiver(name, fname, bitmap_path, small_bitmap)

        fname = self.m_staticText_blrlm_stock.GetLabelText()
        stock = BLReviveStock(None, fname)

        fname = self.m_staticText_blrlm_barrel.GetLabelText()
        barrel = BLReviveBarrel(None, fname)

        fname = self.m_staticText_blrlm_scope.GetLabelText()
        scope = BLReviveScope(None, fname)

        return BLReviveWeapon(name, receiver, stock, barrel, scope)

# --------------------------------------------------------------------------- #

    def load_blrevive_weapon(self, weapon):
        ui_path = 'resource/FoxGame/Content/Packages/UI2/'

        if weapon.receiver.GetImageIconPath() is not None:
            bitmap = wx.Image.ConvertToBitmap(wx.Image(resource_path(ui_path + weapon.receiver.GetImageIconPath())).Scale(64, 32))
            self.m_bitmap_blrlm_receiver.SetBitmap(bitmap)
        self.m_staticText_blrlm_receiver.SetLabel(weapon.receiver.GetFriendlyName())

        if weapon.stock.GetImageIconPath() is not None:
            bitmap = wx.Image.ConvertToBitmap(wx.Image(resource_path(ui_path + weapon.stock.GetImageIconPath())).Scale(64, 32))
            self.m_bitmap_blrlm_stock.SetBitmap(bitmap)
        self.m_staticText_blrlm_stock.SetLabel(weapon.stock.GetFriendlyName())

        if weapon.barrel.GetImageIconPath() is not None:
            bitmap = wx.Image.ConvertToBitmap(wx.Image(resource_path(ui_path + weapon.barrel.GetImageIconPath())).Scale(64, 32))
            self.m_bitmap_blrlm_barrel.SetBitmap(bitmap)
        self.m_staticText_blrlm_barrel.SetLabel(weapon.barrel.GetFriendlyName())

        if weapon.scope.GetImageIconPath() is not None:
            bitmap = wx.Image.ConvertToBitmap(wx.Image(resource_path(ui_path + weapon.scope.GetImageIconPath())).Scale(64, 32))
            self.m_bitmap_blrlm_scope.SetBitmap(bitmap)
        self.m_staticText_blrlm_scope.SetLabel(weapon.scope.GetFriendlyName())

# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #

    def clear_equipped_weapon(self):
        self.m_staticText_blrlm_receiver.SetLabel('')
        self.m_bitmap_blrlm_receiver.SetBitmap(wx.NullBitmap)

        self.m_staticText_blrlm_stock.SetLabel('')
        self.m_bitmap_blrlm_stock.SetBitmap(wx.NullBitmap)

        self.m_staticText_blrlm_barrel.SetLabel('')
        self.m_bitmap_blrlm_barrel.SetBitmap(wx.NullBitmap)

        self.m_staticText_blrlm_scope.SetLabel('')
        self.m_bitmap_blrlm_scope.SetBitmap(wx.NullBitmap)

# --------------------------------------------------------------------------- #

    def handle_gear_toggle(self, source):
        # Untoggle any other gear toggles and load the correct data
        if source != 'm_bmToggleBtn_blrlm_receiver':
            self.m_bmToggleBtn_blrlm_receiver.SetValue(False)
        else:
            self.listctrl_load_receivers()

        if source != 'm_bmToggleBtn_blrlm_stock':
            self.m_bmToggleBtn_blrlm_stock.SetValue(False)
        else:
            self.listctrl_load_stocks()

        if source != 'm_bmToggleBtn_blrlm_barrel':
            self.m_bmToggleBtn_blrlm_barrel.SetValue(False)
        else:
            self.listctrl_load_barrels()

        if source != 'm_bmToggleBtn_blrlm_scope':
            self.m_bmToggleBtn_blrlm_scope.SetValue(False)
        else:
            self.listctrl_load_scopes()

# --------------------------------------------------------------------------- #

    def listctrl_switch_loadout(self, source):
        if source == self.active_loadout:
            return False

        self.loadouts[self.active_loadout] = self.create_blrevive_weapon(self.active_loadout)

        if source in self.loadouts:
            self.load_blrevive_weapon(self.loadouts[source])

        else:
            self.clear_equipped_weapon()

        self.update_main_preview_image(wx.NullBitmap)
        self.active_loadout = source
        self.export_current_loadouts()

# --------------------------------------------------------------------------- #

    def handle_loadout_toggle(self, source):
        # Untoggle any other loadout toggles, save, then load the correct data
        if source != 'm_bmToggleBtnPrimary1':
            self.m_bmToggleBtnPrimary1.SetValue(False)

        if source != 'm_bmToggleBtnPrimary2':
            self.m_bmToggleBtnPrimary2.SetValue(False)

        if source != 'm_bmToggleBtnPrimary3':
            self.m_bmToggleBtnPrimary3.SetValue(False)

        if source != 'm_bmToggleBtnSecondary1':
            self.m_bmToggleBtnSecondary1.SetValue(False)

        if source != 'm_bmToggleBtnSecondary2':
            self.m_bmToggleBtnSecondary2.SetValue(False)

        if source != 'm_bmToggleBtnSecondary3':
            self.m_bmToggleBtnSecondary3.SetValue(False)

        self.listctrl_switch_loadout(source)

# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #

    def export_current_loadouts(self):
        player_name = self.user_settings['PlayerName']
        self.loadouts[self.active_loadout] = self.create_blrevive_weapon()
        empty_weapon = BLReviveWeapon.EmptyWeapon()
        if 'm_bmToggleBtnPrimary1' in self.loadouts:
            p1 = self.loadouts['m_bmToggleBtnPrimary1']
        else:
            p1 = empty_weapon
        if 'm_bmToggleBtnSecondary1' in self.loadouts:
            s1 = self.loadouts['m_bmToggleBtnSecondary1']
        else:
            s1 = empty_weapon

        if 'm_bmToggleBtnPrimary2' in self.loadouts:
            p2 = self.loadouts['m_bmToggleBtnPrimary2']
        else:
            p2 = BLReviveWeapon.EmptyWeapon()
        if 'm_bmToggleBtnSecondary2' in self.loadouts:
            s2 = self.loadouts['m_bmToggleBtnSecondary2']
        else:
            s2 = empty_weapon

        if 'm_bmToggleBtnPrimary3' in self.loadouts:
            p3 = self.loadouts['m_bmToggleBtnPrimary3']
        else:
            p3 = empty_weapon
        if 'm_bmToggleBtnSecondary3' in self.loadouts:
            s3 = self.loadouts['m_bmToggleBtnSecondary3']
        else:
            s3 = empty_weapon

        loadout1 = BLReviveLoadout('loadout1', p1, s1, None, None, None, None, None)
        loadout2 = BLReviveLoadout('loadout2', p2, s2, None, None, None, None, None)
        loadout3 = BLReviveLoadout('loadout3', p3, s3, None, None, None, None, None)
        loadout_json = blrtk.build_magicow_loadout(player_name, loadout1, loadout2, loadout3)

        self.m_scintilla1.Freeze()
        self.m_scintilla1.ClearAll()
        self.m_scintilla1.SetEditable(True)
        self.m_scintilla1.SetText(loadout_json)
        self.m_scintilla1.SetEditable(False)
        self.m_scintilla1.Thaw()

# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #

    # Virtual event handler overrides
    def m_bmToggleBtn_blrlm_receiverOnToggleButton(self, event):
        # print(self.m_bmToggleBtn_blrlm_receiver.GetValue())
        if self.m_bmToggleBtn_blrlm_receiver.GetValue():
            self.handle_gear_toggle('m_bmToggleBtn_blrlm_receiver')
        else:
            self.m_bmToggleBtn_blrlm_receiver.SetValue(True)
        event.Skip()

    def m_bmToggleBtn_blrlm_stockOnToggleButton(self, event):
        if self.m_bmToggleBtn_blrlm_stock.GetValue():
            self.handle_gear_toggle('m_bmToggleBtn_blrlm_stock')
        else:
            self.m_bmToggleBtn_blrlm_stock.SetValue(True)
        event.Skip()

    def m_bmToggleBtn_blrlm_barrelOnToggleButton(self, event):
        if self.m_bmToggleBtn_blrlm_barrel.GetValue():
            self.handle_gear_toggle('m_bmToggleBtn_blrlm_barrel')
        else:
            self.m_bmToggleBtn_blrlm_barrel.SetValue(True)
        event.Skip()

    def m_bmToggleBtn_blrlm_scopeOnToggleButton(self, event):
        if self.m_bmToggleBtn_blrlm_scope.GetValue():
            self.handle_gear_toggle('m_bmToggleBtn_blrlm_scope')
        else:
            self.m_bmToggleBtn_blrlm_scope.SetValue(True)
        event.Skip()

# --------------------------------------------------------------------------- #

    def m_bmToggleBtnLoadout1OnToggleButton(self, event):
        event.Skip()

    def m_bmToggleBtnLoadout2OnToggleButton(self, event):
        event.Skip()

    def m_bmToggleBtnLoadout3OnToggleButton(self, event):
        event.Skip()

# --------------------------------------------------------------------------- #

    def m_bmToggleBtnPrimary1OnToggleButton(self, event):
        if self.m_bmToggleBtnPrimary1.GetValue():
            self.handle_loadout_toggle('m_bmToggleBtnPrimary1')
        else:
            self.m_bmToggleBtnPrimary1.SetValue(True)
        event.Skip()

    def m_bmToggleBtnSecondary1OnToggleButton(self, event):
        if self.m_bmToggleBtnSecondary1.GetValue():
            self.handle_loadout_toggle('m_bmToggleBtnSecondary1')
        else:
            self.m_bmToggleBtnSecondary1.SetValue(True)
        event.Skip()

    def m_bmToggleBtnPrimary2OnToggleButton(self, event):
        if self.m_bmToggleBtnPrimary2.GetValue():
            self.handle_loadout_toggle('m_bmToggleBtnPrimary2')
        else:
            self.m_bmToggleBtnPrimary2.SetValue(True)
        event.Skip()

    def m_bmToggleBtnSecondary2OnToggleButton(self, event):
        if self.m_bmToggleBtnSecondary2.GetValue():
            self.handle_loadout_toggle('m_bmToggleBtnSecondary2')
        else:
            self.m_bmToggleBtnSecondary2.SetValue(True)
        event.Skip()

    def m_bmToggleBtnPrimary3OnToggleButton(self, event):
        if self.m_bmToggleBtnPrimary3.GetValue():
            self.handle_loadout_toggle('m_bmToggleBtnPrimary3')
        else:
            self.m_bmToggleBtnPrimary3.SetValue(True)
        event.Skip()

    def m_bmToggleBtnSecondary3OnToggleButton(self, event):
        if self.m_bmToggleBtnSecondary3.GetValue():
            self.handle_loadout_toggle('m_bmToggleBtnSecondary3')
        else:
            self.m_bmToggleBtnSecondary3.SetValue(True)
        event.Skip()

# --------------------------------------------------------------------------- #

    def m_listCtrl_blrlm_selectorOnListItemActivated(self, event):
        self.ln.dbwp(f'List Item Activated Event: {str(event)}')
        self.set_equipped_gear(event)
        event.Skip()

    def m_listCtrl_blrlm_selectorOnListItemFocused(self, event):
        self.ln.dbwp(f'List Item Focused Event: {str(event)}')
        ui_path = 'resource/FoxGame/Content/Packages/UI2/'
        bitmap_path = self.df_primary.query('FriendlyName == @event.GetText()')
        if not bitmap_path.empty:
            bitmap_path = bitmap_path.iloc[0].ImageIconRef
            bitmap_path = bitmap_path.replace('.', '/') + '.TGA'
            self.ln.dbwp(bitmap_path)
            bitmap = wx.Bitmap(resource_path(ui_path + bitmap_path), wx.BITMAP_TYPE_ANY)
            self.update_main_preview_image(bitmap)
        event.Skip()

# --------------------------------------------------------------------------- #

    def m_button_export_loadoutOnButtonClick(self, event):
        self.export_current_loadouts()
        event.Skip()

    def m_scintilla1OnLeftDClick(self, event):
        # Copy the text to clipboard on a double click
        copy(self.m_scintilla1.GetText())
        event.Skip()


# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #


class wxApp_LocaleFix(wx.App):
    def InitLocale(self):
        """
        Try to ensure that the C and Python locale is in sync with the wxWidgets
        locale on Windows. If you have troubles from the default behavior of this
        method you can override it in a derived class to behave differently.
        Please report the problem you encountered.
        """
        self.ResetLocale()
        if 'wxMSW' in wx.PlatformInfo:
            import locale
            try:
                lang, enc = locale.getdefaultlocale()
                self._initial_locale = wx.Locale(lang, lang[:2], lang)
                # locale.setlocale(locale.LC_ALL, lang)
                locale.setlocale(locale.LC_ALL, 'C')
            except (ValueError, locale.Error) as ex:
                target = wx.LogStderr()
                orig = wx.Log.SetActiveTarget(target)
                print("Unable to set default locale: '{}'".format(ex))
                wx.LogError("Unable to set default locale: '{}'".format(ex))
                wx.Log.SetActiveTarget(orig)


def start_app(parent=None, logfile=None, debug=False):
    """
    Create the app, the frame, show it, and start the event loop.

    Parameters
    ----------
    parent : object, optional
        Parent object of the app frame. The default is None.
    logfile : str, optional
        Path to a file to write any print statements to.
    debug : bool, optional
        Flag to enable debug print statements.

    Returns
    -------
    None.

    """
    # app = wx.App()
    app = wxApp_LocaleFix()
    frm = BLRFrame(parent, logfile, debug)
    frm.post_init()
    frm.Show()
    app.MainLoop()


# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #


if __name__ == '__main__':
    parser = __build_parser()
    args = parser.parse_args()
    logfile = wsobj.implement_outfile_parser(args)

    try:
        # Update the text on the splash screen
        # pyi_splash.update_text()

        # Close the splash screen. It does not matter when the call
        # to this function is made, the splash screen remains open until
        # this function is called or the Python program is terminated.
        pyi_splash.close()
    except Exception:
        pass

    start_app(None, logfile, args.debug)
