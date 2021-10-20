# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.0-35-gd79d7781)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

from bitmap_panel import BitmapPanel
from part_select_panel import PartSelectPanel
import wx
import wx.xrc
import wx.stc

###########################################################################
## Class BLR_LMGR_FRAME
###########################################################################

class BLR_LMGR_FRAME ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"BLRevive Loadout Manager", pos = wx.DefaultPosition, size = wx.Size( 1280,720 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.Colour( 0, 0, 64 ) )

        bSizer_blrlm_main = wx.BoxSizer( wx.HORIZONTAL )

        bSizer3 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel_blrlm_preview = BitmapPanel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_STATIC|wx.TAB_TRAVERSAL )
        self.m_panel_blrlm_preview.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )

        bSizer_blrlm_preview = wx.BoxSizer( wx.VERTICAL )

        bSizer_blrlm_preview.SetMinSize( wx.Size( 420,-1 ) )
        self.m_bitmap_blrlm_preview = wx.StaticBitmap( self.m_panel_blrlm_preview, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 260,132 ), wx.BORDER_SIMPLE )
        bSizer_blrlm_preview.Add( self.m_bitmap_blrlm_preview, 0, wx.ALIGN_CENTER|wx.ALL|wx.FIXED_MINSIZE, 4 )


        self.m_panel_blrlm_preview.SetSizer( bSizer_blrlm_preview )
        self.m_panel_blrlm_preview.Layout()
        bSizer_blrlm_preview.Fit( self.m_panel_blrlm_preview )
        bSizer3.Add( self.m_panel_blrlm_preview, 0, wx.FIXED_MINSIZE|wx.LEFT|wx.RIGHT|wx.TOP, 8 )

        self.m_panel_partselect = BitmapPanel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_STATIC|wx.TAB_TRAVERSAL )
        self.m_panel_partselect.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )

        bSizer19 = wx.BoxSizer( wx.VERTICAL )

        bSizerPartSelect = wx.BoxSizer( wx.VERTICAL )

        self.m_pspanel_rec = PartSelectPanel( self.m_panel_partselect, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_SIMPLE )
        bSizerPartSelect.Add( self.m_pspanel_rec, 0, wx.EXPAND |wx.ALL, 4 )

        self.m_pspanel_muz = PartSelectPanel( self.m_panel_partselect, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_SIMPLE )
        bSizerPartSelect.Add( self.m_pspanel_muz, 0, wx.EXPAND |wx.ALL, 4 )

        self.m_pspanel_gri = PartSelectPanel( self.m_panel_partselect, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_SIMPLE )
        bSizerPartSelect.Add( self.m_pspanel_gri, 0, wx.EXPAND |wx.ALL, 4 )

        self.m_pspanel_bar = PartSelectPanel( self.m_panel_partselect, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_SIMPLE )
        bSizerPartSelect.Add( self.m_pspanel_bar, 0, wx.EXPAND |wx.ALL, 4 )

        self.m_pspanel_mag = PartSelectPanel( self.m_panel_partselect, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_SIMPLE )
        bSizerPartSelect.Add( self.m_pspanel_mag, 0, wx.EXPAND |wx.ALL, 4 )

        self.m_pspanel_sco = PartSelectPanel( self.m_panel_partselect, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_SIMPLE )
        bSizerPartSelect.Add( self.m_pspanel_sco, 0, wx.EXPAND |wx.ALL, 4 )

        self.m_pspanel_sto = PartSelectPanel( self.m_panel_partselect, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_SIMPLE )
        bSizerPartSelect.Add( self.m_pspanel_sto, 0, wx.EXPAND |wx.ALL, 4 )

        self.m_pspanel_tag = PartSelectPanel( self.m_panel_partselect, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_SIMPLE )
        bSizerPartSelect.Add( self.m_pspanel_tag, 0, wx.EXPAND |wx.ALL, 4 )

        self.m_pspanel_cam = PartSelectPanel( self.m_panel_partselect, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_SIMPLE )
        bSizerPartSelect.Add( self.m_pspanel_cam, 0, wx.EXPAND |wx.ALL, 4 )


        bSizer19.Add( bSizerPartSelect, 0, wx.EXPAND, 0 )

        bSizer22 = wx.BoxSizer( wx.VERTICAL )

        bSizer24 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_bmToggleBtnLoadout1 = wx.BitmapToggleButton( self.m_panel_partselect, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
        self.m_bmToggleBtnLoadout1.SetValue( True )
        self.m_bmToggleBtnLoadout1.SetBackgroundColour( wx.Colour( 48, 48, 48 ) )
        self.m_bmToggleBtnLoadout1.Enable( False )
        self.m_bmToggleBtnLoadout1.SetMinSize( wx.Size( 130,24 ) )

        bSizer24.Add( self.m_bmToggleBtnLoadout1, 0, wx.LEFT|wx.RIGHT, 2 )


        bSizer24.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_bmToggleBtnLoadout2 = wx.BitmapToggleButton( self.m_panel_partselect, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
        self.m_bmToggleBtnLoadout2.SetBackgroundColour( wx.Colour( 48, 48, 48 ) )
        self.m_bmToggleBtnLoadout2.Enable( False )
        self.m_bmToggleBtnLoadout2.SetMinSize( wx.Size( 130,24 ) )

        bSizer24.Add( self.m_bmToggleBtnLoadout2, 0, wx.LEFT|wx.RIGHT, 2 )


        bSizer24.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_bmToggleBtnLoadout3 = wx.BitmapToggleButton( self.m_panel_partselect, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
        self.m_bmToggleBtnLoadout3.SetBackgroundColour( wx.Colour( 48, 48, 48 ) )
        self.m_bmToggleBtnLoadout3.Enable( False )
        self.m_bmToggleBtnLoadout3.SetMinSize( wx.Size( 130,24 ) )

        bSizer24.Add( self.m_bmToggleBtnLoadout3, 0, wx.LEFT|wx.RIGHT, 2 )


        bSizer22.Add( bSizer24, 0, wx.EXPAND, 0 )

        bSizer21 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer221 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_bmToggleBtnPrimary1 = wx.BitmapToggleButton( self.m_panel_partselect, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
        self.m_bmToggleBtnPrimary1.SetBackgroundColour( wx.Colour( 48, 48, 48 ) )
        self.m_bmToggleBtnPrimary1.SetMinSize( wx.Size( 64,64 ) )

        bSizer221.Add( self.m_bmToggleBtnPrimary1, 0, wx.LEFT|wx.RIGHT|wx.TOP, 2 )

        self.m_bmToggleBtnSecondary1 = wx.BitmapToggleButton( self.m_panel_partselect, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
        self.m_bmToggleBtnSecondary1.SetBackgroundColour( wx.Colour( 48, 48, 48 ) )
        self.m_bmToggleBtnSecondary1.SetMinSize( wx.Size( 64,64 ) )

        bSizer221.Add( self.m_bmToggleBtnSecondary1, 0, wx.BOTTOM|wx.RIGHT|wx.TOP, 2 )


        bSizer21.Add( bSizer221, 0, wx.EXPAND, 5 )


        bSizer21.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        bSizer211 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_bmToggleBtnPrimary2 = wx.BitmapToggleButton( self.m_panel_partselect, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
        self.m_bmToggleBtnPrimary2.SetBackgroundColour( wx.Colour( 48, 48, 48 ) )
        self.m_bmToggleBtnPrimary2.SetMinSize( wx.Size( 64,64 ) )

        bSizer211.Add( self.m_bmToggleBtnPrimary2, 0, wx.LEFT|wx.RIGHT|wx.TOP, 2 )

        self.m_bmToggleBtnSecondary2 = wx.BitmapToggleButton( self.m_panel_partselect, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
        self.m_bmToggleBtnSecondary2.SetBackgroundColour( wx.Colour( 48, 48, 48 ) )
        self.m_bmToggleBtnSecondary2.SetMinSize( wx.Size( 64,64 ) )

        bSizer211.Add( self.m_bmToggleBtnSecondary2, 0, wx.BOTTOM|wx.RIGHT|wx.TOP, 2 )


        bSizer21.Add( bSizer211, 0, wx.EXPAND, 5 )


        bSizer21.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        bSizer2111 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_bmToggleBtnPrimary3 = wx.BitmapToggleButton( self.m_panel_partselect, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
        self.m_bmToggleBtnPrimary3.SetBackgroundColour( wx.Colour( 48, 48, 48 ) )
        self.m_bmToggleBtnPrimary3.SetMinSize( wx.Size( 64,64 ) )

        bSizer2111.Add( self.m_bmToggleBtnPrimary3, 0, wx.LEFT|wx.RIGHT|wx.TOP, 2 )

        self.m_bmToggleBtnSecondary3 = wx.BitmapToggleButton( self.m_panel_partselect, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
        self.m_bmToggleBtnSecondary3.SetBackgroundColour( wx.Colour( 48, 48, 48 ) )
        self.m_bmToggleBtnSecondary3.SetMinSize( wx.Size( 64,64 ) )

        bSizer2111.Add( self.m_bmToggleBtnSecondary3, 0, wx.BOTTOM|wx.RIGHT|wx.TOP, 2 )


        bSizer21.Add( bSizer2111, 0, wx.EXPAND, 5 )


        bSizer22.Add( bSizer21, 1, wx.EXPAND, 5 )


        bSizer19.Add( bSizer22, 0, wx.ALL|wx.EXPAND, 4 )


        self.m_panel_partselect.SetSizer( bSizer19 )
        self.m_panel_partselect.Layout()
        bSizer19.Fit( self.m_panel_partselect )
        bSizer3.Add( self.m_panel_partselect, 1, wx.EXPAND |wx.ALL, 8 )


        bSizer_blrlm_main.Add( bSizer3, 0, wx.EXPAND, 0 )

        bSizer10 = wx.BoxSizer( wx.VERTICAL )

        self.m_listCtrl_blrlm_selector = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_HRULES|wx.LC_REPORT|wx.LC_SINGLE_SEL|wx.BORDER_SIMPLE )
        self.m_listCtrl_blrlm_selector.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
        self.m_listCtrl_blrlm_selector.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        self.m_listCtrl_blrlm_selector.SetMinSize( wx.Size( 720,480 ) )

        bSizer10.Add( self.m_listCtrl_blrlm_selector, 1, wx.BOTTOM|wx.EXPAND|wx.RIGHT|wx.TOP, 8 )

        self.m_panel11 = BitmapPanel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_STATIC )
        bSizer11 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer14 = wx.BoxSizer( wx.VERTICAL )

        bSizer12 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText6 = wx.StaticText( self.m_panel11, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )

        self.m_staticText6.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

        bSizer12.Add( self.m_staticText6, 0, wx.LEFT, 4 )


        bSizer14.Add( bSizer12, 1, wx.EXPAND, 5 )


        bSizer11.Add( bSizer14, 1, wx.EXPAND, 5 )

        bSizer15 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer15.SetMinSize( wx.Size( 512,-1 ) )
        self.m_panel121 = wx.Panel( self.m_panel11, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panel121.Enable( False )
        self.m_panel121.Hide()

        bSizer121 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText61 = wx.StaticText( self.m_panel121, wx.ID_ANY, u"Export Path:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText61.Wrap( -1 )

        self.m_staticText61.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
        self.m_staticText61.Enable( False )
        self.m_staticText61.Hide()

        bSizer121.Add( self.m_staticText61, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 4 )

        self.m_dirPicker1 = wx.DirPickerCtrl( self.m_panel121, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DIR_MUST_EXIST|wx.DIRP_USE_TEXTCTRL )
        self.m_dirPicker1.Enable( False )
        self.m_dirPicker1.Hide()

        bSizer121.Add( self.m_dirPicker1, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 4 )

        self.m_button_export_loadout = wx.Button( self.m_panel121, wx.ID_ANY, u"Generate Loadout", wx.DefaultPosition, wx.DefaultSize, 0|wx.BORDER_THEME )
        bSizer121.Add( self.m_button_export_loadout, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 4 )


        self.m_panel121.SetSizer( bSizer121 )
        self.m_panel121.Layout()
        bSizer121.Fit( self.m_panel121 )
        bSizer15.Add( self.m_panel121, 0, wx.ALL, 4 )

        self.m_scintilla1 = wx.stc.StyledTextCtrl( self.m_panel11, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_scintilla1.SetUseTabs ( False )
        self.m_scintilla1.SetTabWidth ( 4 )
        self.m_scintilla1.SetIndent ( 4 )
        self.m_scintilla1.SetTabIndents( True )
        self.m_scintilla1.SetBackSpaceUnIndents( True )
        self.m_scintilla1.SetViewEOL( False )
        self.m_scintilla1.SetViewWhiteSpace( False )
        self.m_scintilla1.SetMarginWidth( 2, 0 )
        self.m_scintilla1.SetIndentationGuides( False )
        self.m_scintilla1.SetReadOnly( False );
        self.m_scintilla1.SetMarginWidth( 1, 0 )
        self.m_scintilla1.SetMarginWidth ( 0, 0 )
        self.m_scintilla1.MarkerDefine( wx.stc.STC_MARKNUM_FOLDER, wx.stc.STC_MARK_BOXPLUS )
        self.m_scintilla1.MarkerSetBackground( wx.stc.STC_MARKNUM_FOLDER, wx.BLACK)
        self.m_scintilla1.MarkerSetForeground( wx.stc.STC_MARKNUM_FOLDER, wx.WHITE)
        self.m_scintilla1.MarkerDefine( wx.stc.STC_MARKNUM_FOLDEROPEN, wx.stc.STC_MARK_BOXMINUS )
        self.m_scintilla1.MarkerSetBackground( wx.stc.STC_MARKNUM_FOLDEROPEN, wx.BLACK )
        self.m_scintilla1.MarkerSetForeground( wx.stc.STC_MARKNUM_FOLDEROPEN, wx.WHITE )
        self.m_scintilla1.MarkerDefine( wx.stc.STC_MARKNUM_FOLDERSUB, wx.stc.STC_MARK_EMPTY )
        self.m_scintilla1.MarkerDefine( wx.stc.STC_MARKNUM_FOLDEREND, wx.stc.STC_MARK_BOXPLUS )
        self.m_scintilla1.MarkerSetBackground( wx.stc.STC_MARKNUM_FOLDEREND, wx.BLACK )
        self.m_scintilla1.MarkerSetForeground( wx.stc.STC_MARKNUM_FOLDEREND, wx.WHITE )
        self.m_scintilla1.MarkerDefine( wx.stc.STC_MARKNUM_FOLDEROPENMID, wx.stc.STC_MARK_BOXMINUS )
        self.m_scintilla1.MarkerSetBackground( wx.stc.STC_MARKNUM_FOLDEROPENMID, wx.BLACK)
        self.m_scintilla1.MarkerSetForeground( wx.stc.STC_MARKNUM_FOLDEROPENMID, wx.WHITE)
        self.m_scintilla1.MarkerDefine( wx.stc.STC_MARKNUM_FOLDERMIDTAIL, wx.stc.STC_MARK_EMPTY )
        self.m_scintilla1.MarkerDefine( wx.stc.STC_MARKNUM_FOLDERTAIL, wx.stc.STC_MARK_EMPTY )
        self.m_scintilla1.SetSelBackground( True, wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT ) )
        self.m_scintilla1.SetSelForeground( True, wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
        bSizer15.Add( self.m_scintilla1, 1, wx.ALL|wx.EXPAND, 4 )


        bSizer11.Add( bSizer15, 0, wx.EXPAND, 5 )


        self.m_panel11.SetSizer( bSizer11 )
        self.m_panel11.Layout()
        bSizer11.Fit( self.m_panel11 )
        bSizer10.Add( self.m_panel11, 1, wx.BOTTOM|wx.EXPAND|wx.RIGHT, 8 )


        bSizer_blrlm_main.Add( bSizer10, 1, wx.EXPAND, 0 )


        self.SetSizer( bSizer_blrlm_main )
        self.Layout()
        self.m_menubar1 = wx.MenuBar( 0|wx.BORDER_THEME|wx.CLIP_CHILDREN )
        self.file = wx.Menu()
        self.m_menuItem_file_playername = wx.MenuItem( self.file, wx.ID_ANY, u"Change Player Name", wx.EmptyString, wx.ITEM_NORMAL )
        self.file.Append( self.m_menuItem_file_playername )
        self.m_menuItem_file_playername.Enable( False )

        self.m_menuItem_file_clearloadouts = wx.MenuItem( self.file, wx.ID_ANY, u"Clear All Loadouts", wx.EmptyString, wx.ITEM_NORMAL )
        self.file.Append( self.m_menuItem_file_clearloadouts )
        self.m_menuItem_file_clearloadouts.Enable( False )

        self.m_menuItem_file_savesession = wx.MenuItem( self.file, wx.ID_ANY, u"Save Session", wx.EmptyString, wx.ITEM_NORMAL )
        self.file.Append( self.m_menuItem_file_savesession )

        self.m_menuItem_file_loadsession = wx.MenuItem( self.file, wx.ID_ANY, u"Load Session", wx.EmptyString, wx.ITEM_NORMAL )
        self.file.Append( self.m_menuItem_file_loadsession )

        self.m_menuItem_file_autosave = wx.MenuItem( self.file, wx.ID_ANY, u"Save Session on Exit", wx.EmptyString, wx.ITEM_CHECK )
        self.file.Append( self.m_menuItem_file_autosave )
        self.m_menuItem_file_autosave.Check( True )

        self.m_menubar1.Append( self.file, u"File" )

        self.edit = wx.Menu()
        self.m_menuItem_edit_swapweapon = wx.MenuItem( self.edit, wx.ID_ANY, u"Swap Weapon", wx.EmptyString, wx.ITEM_NORMAL )
        self.edit.Append( self.m_menuItem_edit_swapweapon )
        self.m_menuItem_edit_swapweapon.Enable( False )

        self.m_menubar1.Append( self.edit, u"Edit" )

        self.view = wx.Menu()
        self.m_menuItem_view_0 = wx.MenuItem( self.view, wx.ID_ANY, u"Some checkbox thing", wx.EmptyString, wx.ITEM_CHECK )
        self.view.Append( self.m_menuItem_view_0 )
        self.m_menuItem_view_0.Enable( False )

        self.m_menubar1.Append( self.view, u"View" )

        self.tools = wx.Menu()
        self.m_menubar1.Append( self.tools, u"Tools" )

        self.help = wx.Menu()
        self.m_menuItem_about = wx.MenuItem( self.help, wx.ID_ANY, u"About", wx.EmptyString, wx.ITEM_NORMAL )
        self.help.Append( self.m_menuItem_about )
        self.m_menuItem_about.Enable( False )

        self.m_menubar1.Append( self.help, u"Help" )

        self.SetMenuBar( self.m_menubar1 )


        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_CLOSE, self.BLR_LMGR_FRAMEOnClose )
        self.m_bmToggleBtnLoadout1.Bind( wx.EVT_TOGGLEBUTTON, self.m_bmToggleBtnLoadout1OnToggleButton )
        self.m_bmToggleBtnLoadout2.Bind( wx.EVT_TOGGLEBUTTON, self.m_bmToggleBtnLoadout2OnToggleButton )
        self.m_bmToggleBtnLoadout3.Bind( wx.EVT_TOGGLEBUTTON, self.m_bmToggleBtnLoadout3OnToggleButton )
        self.m_bmToggleBtnPrimary1.Bind( wx.EVT_TOGGLEBUTTON, self.m_bmToggleBtnPrimary1OnToggleButton )
        self.m_bmToggleBtnSecondary1.Bind( wx.EVT_TOGGLEBUTTON, self.m_bmToggleBtnSecondary1OnToggleButton )
        self.m_bmToggleBtnPrimary2.Bind( wx.EVT_TOGGLEBUTTON, self.m_bmToggleBtnPrimary2OnToggleButton )
        self.m_bmToggleBtnSecondary2.Bind( wx.EVT_TOGGLEBUTTON, self.m_bmToggleBtnSecondary2OnToggleButton )
        self.m_bmToggleBtnPrimary3.Bind( wx.EVT_TOGGLEBUTTON, self.m_bmToggleBtnPrimary3OnToggleButton )
        self.m_bmToggleBtnSecondary3.Bind( wx.EVT_TOGGLEBUTTON, self.m_bmToggleBtnSecondary3OnToggleButton )
        self.m_listCtrl_blrlm_selector.Bind( wx.EVT_LIST_ITEM_ACTIVATED, self.m_listCtrl_blrlm_selectorOnListItemActivated )
        self.m_listCtrl_blrlm_selector.Bind( wx.EVT_LIST_ITEM_FOCUSED, self.m_listCtrl_blrlm_selectorOnListItemFocused )
        self.m_button_export_loadout.Bind( wx.EVT_BUTTON, self.m_button_export_loadoutOnButtonClick )
        self.m_scintilla1.Bind( wx.EVT_LEFT_DCLICK, self.m_scintilla1OnLeftDClick )
        self.Bind( wx.EVT_MENU, self.m_menuItem_file_playernameOnMenuSelection, id = self.m_menuItem_file_playername.GetId() )
        self.Bind( wx.EVT_MENU, self.m_menuItem_file_clearloadoutsOnMenuSelection, id = self.m_menuItem_file_clearloadouts.GetId() )
        self.Bind( wx.EVT_MENU, self.m_menuItem_file_savesessionOnMenuSelection, id = self.m_menuItem_file_savesession.GetId() )
        self.Bind( wx.EVT_MENU, self.m_menuItem_file_loadsessionOnMenuSelection, id = self.m_menuItem_file_loadsession.GetId() )
        self.Bind( wx.EVT_MENU, self.m_menuItem_file_autosaveOnMenuSelection, id = self.m_menuItem_file_autosave.GetId() )
        self.Bind( wx.EVT_MENU, self.m_menuItem_aboutOnMenuSelection, id = self.m_menuItem_about.GetId() )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def BLR_LMGR_FRAMEOnClose( self, event ):
        event.Skip()

    def m_bmToggleBtnLoadout1OnToggleButton( self, event ):
        event.Skip()

    def m_bmToggleBtnLoadout2OnToggleButton( self, event ):
        event.Skip()

    def m_bmToggleBtnLoadout3OnToggleButton( self, event ):
        event.Skip()

    def m_bmToggleBtnPrimary1OnToggleButton( self, event ):
        event.Skip()

    def m_bmToggleBtnSecondary1OnToggleButton( self, event ):
        event.Skip()

    def m_bmToggleBtnPrimary2OnToggleButton( self, event ):
        event.Skip()

    def m_bmToggleBtnSecondary2OnToggleButton( self, event ):
        event.Skip()

    def m_bmToggleBtnPrimary3OnToggleButton( self, event ):
        event.Skip()

    def m_bmToggleBtnSecondary3OnToggleButton( self, event ):
        event.Skip()

    def m_listCtrl_blrlm_selectorOnListItemActivated( self, event ):
        event.Skip()

    def m_listCtrl_blrlm_selectorOnListItemFocused( self, event ):
        event.Skip()

    def m_button_export_loadoutOnButtonClick( self, event ):
        event.Skip()

    def m_scintilla1OnLeftDClick( self, event ):
        event.Skip()

    def m_menuItem_file_playernameOnMenuSelection( self, event ):
        event.Skip()

    def m_menuItem_file_clearloadoutsOnMenuSelection( self, event ):
        event.Skip()

    def m_menuItem_file_savesessionOnMenuSelection( self, event ):
        event.Skip()

    def m_menuItem_file_loadsessionOnMenuSelection( self, event ):
        event.Skip()

    def m_menuItem_file_autosaveOnMenuSelection( self, event ):
        event.Skip()

    def m_menuItem_aboutOnMenuSelection( self, event ):
        event.Skip()


