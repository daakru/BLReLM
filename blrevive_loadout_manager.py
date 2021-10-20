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
from blrevive_enums import Gear, UIGear, UIAttachment
import blrevive_toolkit as blrtk
from __WXFB_BLR_LMGR import BLR_LMGR_FRAME
from helpers_pyinstaller import resource_path
from blrevive_gear import BLReviveLoadout, BLReviveWeapon, BLReviveReceiver, BLReviveStock, BLReviveBarrel, BLReviveScope, BLReviveMuzzle, BLReviveMagazine, BLReviveGrip, BLReviveTag, BLReviveCamo


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

        self.part_select_panels = [
            self.m_pspanel_rec,
            self.m_pspanel_muz,
            self.m_pspanel_gri,
            self.m_pspanel_bar,
            self.m_pspanel_mag,
            self.m_pspanel_sco,
            self.m_pspanel_sto,
            self.m_pspanel_tag,
            self.m_pspanel_cam
        ]

        self.gear_slots = blrtk.load_saved_session()
        self.active_loadout = Gear.P1
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

        self.muzzle_columns = self.receiver_columns.copy()
        self.muzzle_columns[0] = 'Muzzle'

        self.magazine_columns = self.receiver_columns.copy()
        self.magazine_columns[0] = 'Magazine'

        self.grip_columns = self.receiver_columns.copy()
        self.grip_columns[0] = 'Grip'

        self.tag_columns = self.receiver_columns.copy()
        self.tag_columns[0] = 'Tag'

        self.camo_columns = self.receiver_columns.copy()
        self.camo_columns[0] = 'Camo'

        # Lazy mode for now to get exporting to MagiCow functional
        self.temp_attachments = {}
        self.temp_attachments[UIAttachment.RECEIVER.name] = [blrtk.get_receivers(), self.receiver_columns]
        self.temp_attachments[UIAttachment.MUZZLE.name] = [blrtk.get_muzzles(), self.muzzle_columns]
        self.temp_attachments[UIAttachment.GRIP.name] = [blrtk.get_grips(), self.grip_columns]
        self.temp_attachments[UIAttachment.BARREL.name] = [blrtk.get_barrels(), self.barrel_columns]
        self.temp_attachments[UIAttachment.MAGAZINE.name] = [blrtk.get_magazines(), self.magazine_columns]
        self.temp_attachments[UIAttachment.SCOPE.name] = [blrtk.get_scopes(), self.scope_columns]
        self.temp_attachments[UIAttachment.STOCK.name] = [blrtk.get_stocks(), self.stock_columns]
        self.temp_attachments[UIAttachment.TAG.name] = [[], self.tag_columns]
        self.temp_attachments[UIAttachment.CAMO.name] = [[], self.camo_columns]

        self.temp_receivers = blrtk.get_receivers()

        self.temp_stocks = blrtk.get_stocks()

        self.temp_barrels = blrtk.get_barrels()

        self.temp_scopes = blrtk.get_scopes()

        self.temp_muzzles = blrtk.get_muzzles()

        self.temp_grips = blrtk.get_grips()

        self.temp_magazines = blrtk.get_magazines()

        self.temp_tags = []

        self.temp_camos = []

        # self.muzzle_idx = 0
        # self.magazine_idx = -1

        self.df_primary = blrtk.build_receivers_dataframe()

# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #

        # self.m_panel_partselect.Freeze()
        # self.m_panel_partselect.Thaw()

# --------------------------------------------------------------------------- #

        # Scintilla
        # print(f'Lexer: {self.m_scintilla1.GetLexer()}')
        self.m_scintilla1.StyleSetFont(0, self.font_blr_UI_12)
        self.m_scintilla1.SetUseHorizontalScrollBar(False)
        self.m_scintilla1.SetLexer(wx.stc.STC_LEX_CONF)
        # self.m_scintilla1.SetVScrollBar() SetMouseWheelCaptures SetMouseDownCaptures

# --------------------------------------------------------------------------- #

        # List Control
        headerattr = wx.ItemAttr()
        headerattr.SetFont(self.font_blr_UI_14)
        self.m_listCtrl_blrlm_selector.SetHeaderAttr(headerattr)
        self.m_bitmap_blrlm_preview.SetBackgroundColour(wx.Colour(0, 64, 128))

# --------------------------------------------------------------------------- #

        # Bitmap Panels
        self.m_panel_blrlm_preview.SetPanelBitmapPositionToParent()
        self.m_panel_partselect.SetPanelBitmapPositionToParent()
        self.m_panel11.SetPanelBitmapPositionToParent()

# --------------------------------------------------------------------------- #

        # RECEIVER
        self.m_pspanel_rec.set_part(UIAttachment.RECEIVER)

        # MUZZLE
        self.m_pspanel_muz.set_part(UIAttachment.MUZZLE)

        # GRIP
        self.m_pspanel_gri.set_part(UIAttachment.GRIP)

        # BARREL
        self.m_pspanel_bar.set_part(UIAttachment.BARREL)

        # MAGAZINE
        self.m_pspanel_mag.set_part(UIAttachment.MAGAZINE)

        # SCOPE
        self.m_pspanel_sco.set_part(UIAttachment.SCOPE)

        # STOCK
        self.m_pspanel_sto.set_part(UIAttachment.STOCK)

        # TAG
        self.m_pspanel_tag.set_part(UIAttachment.TAG)

        # CAMO
        self.m_pspanel_cam.set_part(UIAttachment.CAMO)

# --------------------------------------------------------------------------- #

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

# --------------------------------------------------------------------------- #

        self.m_bmToggleBtnLoadout1.SetLabelMarkup('<span face="ProFontWindows" size="14336">LOADOUT 1</span>')
        self.m_bmToggleBtnLoadout2.SetLabelMarkup('<span face="ProFontWindows" size="14336">LOADOUT 2</span>')
        self.m_bmToggleBtnLoadout3.SetLabelMarkup('<span face="ProFontWindows" size="14336">LOADOUT 3</span>')

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

    def listctrl_sort_rows(self):
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
        # self.listctrl_sort_rows()

# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #

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

# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #

    # def post_init(self):
    #     self.listctrl_load_receivers()

# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #

    def set_equipped_gear(self, event):
        fname = event.GetText()
        # data = event.GetItem().GetData()
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

        for psp in self.part_select_panels:
            if psp.ui_toggle.GetValue():
                psp.ui_text.SetLabel(fname)
                psp.ui_bitmap.SetBitmap(bitmap)
                break

        self.export_current_loadouts()

# --------------------------------------------------------------------------- #

    def update_main_preview_image(self, bitmap):
        self.m_bitmap_blrlm_preview.SetBitmap(bitmap)

# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #

    def create_blrevive_weapon(self):
        args = [None]
        for psp in self.part_select_panels:
            fname = psp.ui_text.GetLabelText()
            part = self.df_primary.query('FriendlyName == @fname')
            if not part.empty:
                name = part.iloc[0].WPN
                bitmap_path = (part.iloc[0].ImageIconRef).replace('.', '/') + '.TGA'
                icon_path = (part.iloc[0].ImageIconRef).replace('.', '/') + '.TGA'
            else:
                name = None
                bitmap_path = None
                icon_path = None
            args.append(psp.create_attachment(name, fname, bitmap_path, icon_path))

        return BLReviveWeapon(*args)

# --------------------------------------------------------------------------- #

    def load_blrevive_weapon(self, weapon):
        weapon_dict = weapon.to_enum()
        ui_path = 'resource/FoxGame/Content/Packages/UI2/'

        for enum in [a for a in UIAttachment][1:]:
            img_path = weapon_dict[enum].GetImageIconPath()
            if img_path is not None:
                image = wx.Image(resource_path(ui_path + weapon_dict[enum].GetImageIconPath()))
                self.ln.dbwp(resource_path(ui_path + weapon_dict[enum].GetImageIconPath()))
                if image.GetWidth() == image.GetHeight():
                    image = image.Scale(32, 32)
                else:
                    image = image.Scale(64, 32)
                bitmap = wx.Image.ConvertToBitmap(image)
            else:
                bitmap = wx.NullBitmap
            self.part_select_panels[enum.value - 1].ui_bitmap.SetBitmap(bitmap)
            self.part_select_panels[enum.value - 1].ui_text.SetLabel(weapon_dict[enum].GetFriendlyName())

# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #

    def post_init(self):
        self.listctrl_load_parts(UIAttachment.RECEIVER)
        self.m_pspanel_rec.ui_toggle.SetValue(True)
        # breakpoint()
        if self.active_loadout.name in self.gear_slots:
            self.load_blrevive_weapon(self.gear_slots[self.active_loadout.name])

# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #

    def clear_equipped_weapon(self):
        for psp in self.part_select_panels:
            psp.reset_attachment()

# --------------------------------------------------------------------------- #

    def listctrl_load_parts(self, source):
        # Freeze the display of the control
        self.m_listCtrl_blrlm_selector.Freeze()

        # Clear the existing items
        self.listctrl_clear_rows()

        # Clear the existing columns
        self.listctrl_clear_columns()

        source_data = self.temp_attachments[source.name]

        # Populate the columns for the Camos
        self.listctrl_load_columns(source_data[1])

        # Load Items
        for idx, item in enumerate(source_data[0]):
            self.m_listCtrl_blrlm_selector.Append([item])
            self.m_listCtrl_blrlm_selector.SetItemData(self.m_listCtrl_blrlm_selector.GetItemCount() - 1, idx)

        # Format the items
        self.listctrl_format_items()

        # Thaw the display of the control
        self.m_listCtrl_blrlm_selector.Thaw()

# --------------------------------------------------------------------------- #

    def handle_gear_toggle(self, source):
        for psp in self.part_select_panels:
            if psp.PartID != source:
                psp.ui_toggle.SetValue(False)
        self.listctrl_load_parts(source)
        pass

# --------------------------------------------------------------------------- #

    def listctrl_switch_loadout(self, source):
        """
        Swap the active gear if necessary.

        Parameters
        ----------
        source : Gear
            Gear Enum for the gear slot that should be swapped.

        Returns
        -------
        bool
            Returns False if nothing should be swapped.

        """
        if source == self.active_loadout:
            return False

        self.gear_slots[self.active_loadout.name] = self.create_blrevive_weapon()

        if source.name in self.gear_slots:
            self.load_blrevive_weapon(self.gear_slots[source.name])

        else:
            self.clear_equipped_weapon()

        self.update_main_preview_image(wx.NullBitmap)
        self.active_loadout = source
        self.export_current_loadouts()
        return True

# --------------------------------------------------------------------------- #

    def handle_loadout_toggle(self, source):
        """
        Handler for loadout UI toggle events.

        Parameters
        ----------
        source : UIGear
            UIGear Enum for the UI component this was called from.

        Returns
        -------
        None.

        """
        # Untoggle any other loadout toggles, save, then load the correct data
        if source != UIGear.m_bmToggleBtnPrimary1:
            self.m_bmToggleBtnPrimary1.SetValue(False)

        if source != UIGear.m_bmToggleBtnPrimary2:
            self.m_bmToggleBtnPrimary2.SetValue(False)

        if source != UIGear.m_bmToggleBtnPrimary3:
            self.m_bmToggleBtnPrimary3.SetValue(False)

        if source != UIGear.m_bmToggleBtnSecondary1:
            self.m_bmToggleBtnSecondary1.SetValue(False)

        if source != UIGear.m_bmToggleBtnSecondary2:
            self.m_bmToggleBtnSecondary2.SetValue(False)

        if source != UIGear.m_bmToggleBtnSecondary3:
            self.m_bmToggleBtnSecondary3.SetValue(False)

        self.listctrl_switch_loadout(Gear(source.value))

# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #

    def export_current_loadouts(self):
        player_name = self.user_settings['PlayerName']
        self.gear_slots[self.active_loadout.name] = self.create_blrevive_weapon()
        empty_weapon = BLReviveWeapon.EmptyWeapon()
        if Gear.P1.name in self.gear_slots:
            p1 = self.gear_slots[Gear.P1.name]
        else:
            p1 = empty_weapon
        if Gear.S1.name in self.gear_slots:
            s1 = self.gear_slots[Gear.S1.name]
        else:
            s1 = empty_weapon

        if Gear.P2.name in self.gear_slots:
            p2 = self.gear_slots[Gear.P2.name]
        else:
            p2 = BLReviveWeapon.EmptyWeapon()
        if Gear.S2.name in self.gear_slots:
            s2 = self.gear_slots[Gear.S2.name]
        else:
            s2 = empty_weapon

        if Gear.P3.name in self.gear_slots:
            p3 = self.gear_slots[Gear.P3.name]
        else:
            p3 = empty_weapon
        if Gear.S3.name in self.gear_slots:
            s3 = self.gear_slots[Gear.S3.name]
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
        self.m_scintilla1.StyleSetFont(0, self.font_blr_UI_12)
        self.m_scintilla1.SetEditable(False)
        self.m_scintilla1.Thaw()

    def export_current_session(self):
        self.gear_slots[self.active_loadout.name] = self.create_blrevive_weapon()
        empty_weapon = BLReviveWeapon.EmptyWeapon()
        if Gear.P1.name in self.gear_slots:
            p1 = self.gear_slots[Gear.P1.name]
        else:
            p1 = empty_weapon
        if Gear.S1.name in self.gear_slots:
            s1 = self.gear_slots[Gear.S1.name]
        else:
            s1 = empty_weapon

        if Gear.P2.name in self.gear_slots:
            p2 = self.gear_slots[Gear.P2.name]
        else:
            p2 = BLReviveWeapon.EmptyWeapon()
        if Gear.S2.name in self.gear_slots:
            s2 = self.gear_slots[Gear.S2.name]
        else:
            s2 = empty_weapon

        if Gear.P3.name in self.gear_slots:
            p3 = self.gear_slots[Gear.P3.name]
        else:
            p3 = empty_weapon
        if Gear.S3.name in self.gear_slots:
            s3 = self.gear_slots[Gear.S3.name]
        else:
            s3 = empty_weapon

        session = {Gear.P1.name: p1.to_dict(), Gear.S1.name: s1.to_dict(),
                   Gear.P2.name: p2.to_dict(), Gear.S2.name: s2.to_dict(),
                   Gear.P3.name: p3.to_dict(), Gear.S3.name: s3.to_dict()}

        blrtk.write_saved_session(session)

# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #

    # Virtual event handler overrides
    def BLR_LMGR_FRAMEOnClose(self, event):
        if self.m_menuItem_file_autosave.IsChecked():
            self.export_current_session()
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
            self.handle_loadout_toggle(UIGear.m_bmToggleBtnPrimary1)
        else:
            self.m_bmToggleBtnPrimary1.SetValue(True)
        event.Skip()

    def m_bmToggleBtnSecondary1OnToggleButton(self, event):
        if self.m_bmToggleBtnSecondary1.GetValue():
            self.handle_loadout_toggle(UIGear.m_bmToggleBtnSecondary1)
        else:
            self.m_bmToggleBtnSecondary1.SetValue(True)
        event.Skip()

    def m_bmToggleBtnPrimary2OnToggleButton(self, event):
        if self.m_bmToggleBtnPrimary2.GetValue():
            self.handle_loadout_toggle(UIGear.m_bmToggleBtnPrimary2)
        else:
            self.m_bmToggleBtnPrimary2.SetValue(True)
        event.Skip()

    def m_bmToggleBtnSecondary2OnToggleButton(self, event):
        if self.m_bmToggleBtnSecondary2.GetValue():
            self.handle_loadout_toggle(UIGear.m_bmToggleBtnSecondary2)
        else:
            self.m_bmToggleBtnSecondary2.SetValue(True)
        event.Skip()

    def m_bmToggleBtnPrimary3OnToggleButton(self, event):
        if self.m_bmToggleBtnPrimary3.GetValue():
            self.handle_loadout_toggle(UIGear.m_bmToggleBtnPrimary3)
        else:
            self.m_bmToggleBtnPrimary3.SetValue(True)
        event.Skip()

    def m_bmToggleBtnSecondary3OnToggleButton(self, event):
        if self.m_bmToggleBtnSecondary3.GetValue():
            self.handle_loadout_toggle(UIGear.m_bmToggleBtnSecondary3)
        else:
            self.m_bmToggleBtnSecondary3.SetValue(True)
        event.Skip()

# --------------------------------------------------------------------------- #

    def m_listCtrl_blrlm_selectorOnListItemActivated(self, event):
        self.ln.dbwp(f'List Item Activated Event: {str(event)}')
        # breakpoint()
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
        # self.export_current_loadouts()
        self.export_current_session()

    def m_scintilla1OnLeftDClick(self, event):
        # Copy the text to clipboard on a double click
        copy(self.m_scintilla1.GetText())

    def m_menuItem_file_playernameOnMenuSelection(self, event):
        # TODO: Add dialog box to enter a new player name
        self.user_settings = blrtk.get_user_config()
        event.Skip()

    def m_menuItem_file_clearloadoutsOnMenuSelection(self, event):
        # TODO: Add dialog box to confirm action
        event.Skip()

    def m_menuItem_file_savesessionOnMenuSelection(self, event):
        self.export_current_session()

    def m_menuItem_file_loadsessionOnMenuSelection(self, event):
        self.gear_slots = blrtk.load_saved_session()

        if self.active_loadout.name in self.gear_slots:
            self.load_blrevive_weapon(self.gear_slots[self.active_loadout.name])

        else:
            self.clear_equipped_weapon()

        self.update_main_preview_image(wx.NullBitmap)
        self.export_current_loadouts()

    def m_menuItem_file_autosaveOnMenuSelection(self, event):
        event.Skip()

    def m_menuItem_aboutOnMenuSelection(self, event):
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
                # locale.setlocale(locale.LC_ALL, 'C')
                with open('./launch.log', 'a') as fp:
                    fp.write(f'wxApp_LocaleFix.InitLocale: lang = {lang}\n')
                print(lang)
            except (ValueError, locale.Error) as ex:
                target = wx.LogStderr()
                orig = wx.Log.SetActiveTarget(target)
                with open('./launch.log', 'a') as fp:
                    fp.write(f'wxApp_LocaleFix.InitLocale:except-0 Unable to set default locale: \'{ex}\'\n')
                print("Unable to set default locale: '{}'".format(ex))
                wx.LogError("Unable to set default locale: '{}'".format(ex))
                wx.Log.SetActiveTarget(orig)
            try:
                locale.setlocale(locale.LC_ALL, lang.replace('_', '-'))
            except (ValueError, locale.Error) as ex:
                locale.setlocale(locale.LC_ALL, lang.replace('-', '_'))
                target = wx.LogStderr()
                orig = wx.Log.SetActiveTarget(target)
                with open('./launch.log', 'a') as fp:
                    fp.write(f'wxApp_LocaleFix.InitLocale:except-1 Unable to set default locale: \'{ex}\'\n')
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
    with open('./launch.log', 'w') as fp:
        pass
    # try:
    #     app = wxApp_LocaleFix()

    #     frm = BLRFrame(parent, logfile, debug)
    #     frm.post_init()
    #     frm.Show()
    #     app.MainLoop()
    #     with open('./launch.log', 'w') as fp:
    #         fp.write('Launch with wxApp_LocaleFix.')
    # except AssertionError:
    #     with open('./launch.log', 'w') as fp:
    #         fp.write('Caught Exception: AssertionError. Trying default wxApp.')
    #     app = wx.App()

    #     frm = BLRFrame(parent, logfile, debug)
    #     frm.post_init()
    #     frm.Show()
    #     app.MainLoop()
    app = wxApp_LocaleFix()

    with open('./launch.log', 'a') as fp:
        fp.write('Launch with wxApp_LocaleFix.\n')
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
