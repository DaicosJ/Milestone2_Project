# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

import gettext
_ = gettext.gettext

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"Nutritional Database App"), pos = wx.DefaultPosition, size = wx.Size( 595,389 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        gSizer2 = wx.GridSizer( 0, 2, 0, 0 )

        fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
        fgSizer1.SetFlexibleDirection( wx.BOTH )
        fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, _(u"Protein (g):"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )

        fgSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )

        self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer1.Add( self.m_textCtrl1, 0, wx.ALL, 5 )

        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, _(u"Fat (g):"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )

        fgSizer1.Add( self.m_staticText2, 0, wx.ALL, 5 )

        self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer1.Add( self.m_textCtrl2, 0, wx.ALL, 5 )

        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, _(u"Carbohydrates (g):"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )

        fgSizer1.Add( self.m_staticText3, 0, wx.ALL, 5 )

        self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer1.Add( self.m_textCtrl3, 0, wx.ALL, 5 )

        self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, _(u"Calories:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )

        fgSizer1.Add( self.m_staticText4, 0, wx.ALL, 5 )

        self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer1.Add( self.m_textCtrl4, 0, wx.ALL, 5 )

        sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.HORIZONTAL )

        self.m_button1 = wx.Button( sbSizer2.GetStaticBox(), wx.ID_ANY, _(u"Search"), wx.DefaultPosition, wx.DefaultSize, 0 )
        sbSizer2.Add( self.m_button1, 0, wx.ALL, 5 )

        self.m_button2 = wx.Button( sbSizer2.GetStaticBox(), wx.ID_ANY, _(u"Reset"), wx.DefaultPosition, wx.DefaultSize, 0 )
        sbSizer2.Add( self.m_button2, 0, wx.ALL, 5 )


        fgSizer1.Add( sbSizer2, 0, 0, 0 )


        gSizer2.Add( fgSizer1, 1, 0, 5 )

        self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, _(u"Nutrition Table"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText9.Wrap( -1 )

        gSizer2.Add( self.m_staticText9, 0, wx.ALIGN_BOTTOM, 0 )

        self.m_grid1 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 480,158 ), 0 )

        # Grid
        self.m_grid1.CreateGrid( 5, 5 )
        self.m_grid1.EnableEditing( True )
        self.m_grid1.EnableGridLines( True )
        self.m_grid1.EnableDragGridSize( False )
        self.m_grid1.SetMargins( 0, 0 )

        # Columns
        self.m_grid1.EnableDragColMove( False )
        self.m_grid1.EnableDragColSize( True )
        self.m_grid1.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Rows
        self.m_grid1.EnableDragRowSize( True )
        self.m_grid1.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Label Appearance

        # Cell Defaults
        self.m_grid1.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
        gSizer2.Add( self.m_grid1, 0, 0, 0 )


        self.SetSizer( gSizer2 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_button1.Bind( wx.EVT_BUTTON, self.search_nutritional_values )
        self.m_button2.Bind( wx.EVT_BUTTON, self.reset_filters )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def search_nutritional_values( self, event ):
        event.Skip()

    def reset_filters( self, event ):
        event.Skip()


