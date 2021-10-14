# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.0-35-gd79d7781)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

from bitmap_panel import BitmapPanel
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

        self.m_panel_partselect_re1 = wx.Panel( self.m_panel_partselect, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_SIMPLE )
        self.m_panel_partselect_re1.SetBackgroundColour( wx.Colour( 0, 64, 128 ) )

        bSizerPSRE1 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_bmToggleBtn_blrlm_receiver = wx.BitmapToggleButton( self.m_panel_partselect_re1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 32,32 ), wx.BORDER_NONE )
        self.m_bmToggleBtn_blrlm_receiver.SetValue( True )

        self.m_bmToggleBtn_blrlm_receiver.SetBitmap( wx.NullBitmap )
        self.m_bmToggleBtn_blrlm_receiver.SetBackgroundColour( wx.Colour( 48, 48, 48 ) )

        bSizerPSRE1.Add( self.m_bmToggleBtn_blrlm_receiver, 0, wx.ALL, 0 )

        self.m_bitmap_blrlm_receiver = wx.StaticBitmap( self.m_panel_partselect_re1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_bitmap_blrlm_receiver.SetMinSize( wx.Size( 64,32 ) )
        self.m_bitmap_blrlm_receiver.SetMaxSize( wx.Size( 64,32 ) )

        bSizerPSRE1.Add( self.m_bitmap_blrlm_receiver, 0, wx.LEFT|wx.RIGHT, 8 )

        self.m_staticText_blrlm_receiver = wx.StaticText( self.m_panel_partselect_re1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_blrlm_receiver.Wrap( -1 )

        self.m_staticText_blrlm_receiver.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

        bSizerPSRE1.Add( self.m_staticText_blrlm_receiver, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 0 )


        self.m_panel_partselect_re1.SetSizer( bSizerPSRE1 )
        self.m_panel_partselect_re1.Layout()
        bSizerPSRE1.Fit( self.m_panel_partselect_re1 )
        bSizerPartSelect.Add( self.m_panel_partselect_re1, 0, wx.EXPAND |wx.ALL, 4 )

        self.m_panel_partselect_st1 = wx.Panel( self.m_panel_partselect, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_SIMPLE )
        self.m_panel_partselect_st1.SetBackgroundColour( wx.Colour( 0, 64, 128 ) )

        bSizerPSST1 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_bmToggleBtn_blrlm_stock = wx.BitmapToggleButton( self.m_panel_partselect_st1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 32,32 ), wx.BORDER_NONE )

        self.m_bmToggleBtn_blrlm_stock.SetBitmap( wx.NullBitmap )
        self.m_bmToggleBtn_blrlm_stock.SetBackgroundColour( wx.Colour( 48, 48, 48 ) )

        bSizerPSST1.Add( self.m_bmToggleBtn_blrlm_stock, 0, wx.ALL, 0 )

        self.m_bitmap_blrlm_stock = wx.StaticBitmap( self.m_panel_partselect_st1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_bitmap_blrlm_stock.SetMinSize( wx.Size( 64,32 ) )
        self.m_bitmap_blrlm_stock.SetMaxSize( wx.Size( 64,32 ) )

        bSizerPSST1.Add( self.m_bitmap_blrlm_stock, 0, wx.LEFT|wx.RIGHT, 8 )

        self.m_staticText_blrlm_stock = wx.StaticText( self.m_panel_partselect_st1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_blrlm_stock.Wrap( -1 )

        self.m_staticText_blrlm_stock.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

        bSizerPSST1.Add( self.m_staticText_blrlm_stock, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 0 )


        self.m_panel_partselect_st1.SetSizer( bSizerPSST1 )
        self.m_panel_partselect_st1.Layout()
        bSizerPSST1.Fit( self.m_panel_partselect_st1 )
        bSizerPartSelect.Add( self.m_panel_partselect_st1, 0, wx.EXPAND |wx.ALL, 4 )

        self.m_panel_partselect_ba1 = wx.Panel( self.m_panel_partselect, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_SIMPLE )
        self.m_panel_partselect_ba1.SetBackgroundColour( wx.Colour( 0, 64, 128 ) )

        bSizerPSBA1 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_bmToggleBtn_blrlm_barrel = wx.BitmapToggleButton( self.m_panel_partselect_ba1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 32,32 ), wx.BORDER_NONE )

        self.m_bmToggleBtn_blrlm_barrel.SetBitmap( wx.NullBitmap )
        self.m_bmToggleBtn_blrlm_barrel.SetBackgroundColour( wx.Colour( 48, 48, 48 ) )

        bSizerPSBA1.Add( self.m_bmToggleBtn_blrlm_barrel, 0, wx.ALL, 0 )

        self.m_bitmap_blrlm_barrel = wx.StaticBitmap( self.m_panel_partselect_ba1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_bitmap_blrlm_barrel.SetMinSize( wx.Size( 64,32 ) )
        self.m_bitmap_blrlm_barrel.SetMaxSize( wx.Size( 64,32 ) )

        bSizerPSBA1.Add( self.m_bitmap_blrlm_barrel, 0, wx.LEFT|wx.RIGHT, 8 )

        self.m_staticText_blrlm_barrel = wx.StaticText( self.m_panel_partselect_ba1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_blrlm_barrel.Wrap( -1 )

        self.m_staticText_blrlm_barrel.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

        bSizerPSBA1.Add( self.m_staticText_blrlm_barrel, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 0 )


        self.m_panel_partselect_ba1.SetSizer( bSizerPSBA1 )
        self.m_panel_partselect_ba1.Layout()
        bSizerPSBA1.Fit( self.m_panel_partselect_ba1 )
        bSizerPartSelect.Add( self.m_panel_partselect_ba1, 0, wx.EXPAND |wx.ALL, 5 )

        self.m_panel_partselect_sc1 = wx.Panel( self.m_panel_partselect, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_SIMPLE )
        self.m_panel_partselect_sc1.SetBackgroundColour( wx.Colour( 0, 64, 128 ) )

        bSizerPSSC1 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_bmToggleBtn_blrlm_scope = wx.BitmapToggleButton( self.m_panel_partselect_sc1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 32,32 ), wx.BORDER_NONE )

        self.m_bmToggleBtn_blrlm_scope.SetBitmap( wx.NullBitmap )
        self.m_bmToggleBtn_blrlm_scope.SetBackgroundColour( wx.Colour( 48, 48, 48 ) )

        bSizerPSSC1.Add( self.m_bmToggleBtn_blrlm_scope, 0, wx.ALL, 0 )

        self.m_bitmap_blrlm_scope = wx.StaticBitmap( self.m_panel_partselect_sc1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_bitmap_blrlm_scope.SetMinSize( wx.Size( 64,32 ) )
        self.m_bitmap_blrlm_scope.SetMaxSize( wx.Size( 64,32 ) )

        bSizerPSSC1.Add( self.m_bitmap_blrlm_scope, 0, wx.LEFT|wx.RIGHT, 8 )

        self.m_staticText_blrlm_scope = wx.StaticText( self.m_panel_partselect_sc1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_blrlm_scope.Wrap( -1 )

        self.m_staticText_blrlm_scope.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

        bSizerPSSC1.Add( self.m_staticText_blrlm_scope, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 0 )


        self.m_panel_partselect_sc1.SetSizer( bSizerPSSC1 )
        self.m_panel_partselect_sc1.Layout()
        bSizerPSSC1.Fit( self.m_panel_partselect_sc1 )
        bSizerPartSelect.Add( self.m_panel_partselect_sc1, 0, wx.EXPAND |wx.ALL, 5 )


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
        self.m_menubar1 = wx.MenuBar( 0 )
        self.SetMenuBar( self.m_menubar1 )


        self.Centre( wx.BOTH )

        # Connect Events
        self.m_bmToggleBtn_blrlm_receiver.Bind( wx.EVT_TOGGLEBUTTON, self.m_bmToggleBtn_blrlm_receiverOnToggleButton )
        self.m_bmToggleBtn_blrlm_stock.Bind( wx.EVT_TOGGLEBUTTON, self.m_bmToggleBtn_blrlm_stockOnToggleButton )
        self.m_bmToggleBtn_blrlm_barrel.Bind( wx.EVT_TOGGLEBUTTON, self.m_bmToggleBtn_blrlm_barrelOnToggleButton )
        self.m_bmToggleBtn_blrlm_scope.Bind( wx.EVT_TOGGLEBUTTON, self.m_bmToggleBtn_blrlm_scopeOnToggleButton )
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

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def m_bmToggleBtn_blrlm_receiverOnToggleButton( self, event ):
        event.Skip()

    def m_bmToggleBtn_blrlm_stockOnToggleButton( self, event ):
        event.Skip()

    def m_bmToggleBtn_blrlm_barrelOnToggleButton( self, event ):
        event.Skip()

    def m_bmToggleBtn_blrlm_scopeOnToggleButton( self, event ):
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


