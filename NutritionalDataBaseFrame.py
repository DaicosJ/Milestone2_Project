# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

import gettext
_ = gettext.gettext

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"Nutritional Database App"), pos = wx.DefaultPosition, size = wx.Size( 582,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        gSizer2 = wx.GridSizer( 0, 2, 0, 0 )

        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, _(u"Protein (g):"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )

        gSizer2.Add( self.m_staticText1, 0, wx.ALL, 5 )

        self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer2.Add( self.m_textCtrl1, 0, wx.ALL, 5 )

        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, _(u"Fat (g):"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )

        gSizer2.Add( self.m_staticText2, 0, wx.ALL, 5 )

        self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer2.Add( self.m_textCtrl2, 0, wx.ALL, 5 )

        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, _(u"Carbohydrates (g):"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )

        gSizer2.Add( self.m_staticText3, 0, wx.ALL, 5 )

        self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer2.Add( self.m_textCtrl3, 0, wx.ALL, 5 )

        self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, _(u"Calories:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )

        gSizer2.Add( self.m_staticText4, 0, wx.ALL, 5 )

        self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer2.Add( self.m_textCtrl4, 0, wx.ALL, 5 )

        bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer5.SetMinSize( wx.Size( -3,-3 ) )
        self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, _(u"Protein Range (g):"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )

        bSizer5.Add( self.m_staticText5, 0, wx.ALL, 5 )

        self.m_textCtrl5 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer5.Add( self.m_textCtrl5, 0, wx.ALL, 5 )

        self.m_textCtrl6 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer5.Add( self.m_textCtrl6, 0, wx.ALL, 5 )


        gSizer2.Add( bSizer5, 1, wx.EXPAND, 5 )

        bSizer51 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer51.SetMinSize( wx.Size( -3,-3 ) )
        self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, _(u"Fat Range (g):"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )

        bSizer51.Add( self.m_staticText6, 0, wx.ALL, 5 )

        self.m_textCtrl7 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer51.Add( self.m_textCtrl7, 0, wx.ALL, 5 )

        self.m_textCtrl8 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer51.Add( self.m_textCtrl8, 0, wx.ALL, 5 )


        gSizer2.Add( bSizer51, 1, wx.EXPAND, 5 )

        bSizer52 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer52.SetMinSize( wx.Size( -3,-3 ) )
        self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, _(u"Protein Range (g):"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )

        bSizer52.Add( self.m_staticText7, 0, wx.ALL, 5 )

        self.m_textCtrl9 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer52.Add( self.m_textCtrl9, 0, wx.ALL, 5 )

        self.m_textCtrl10 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer52.Add( self.m_textCtrl10, 0, wx.ALL, 5 )


        gSizer2.Add( bSizer52, 1, wx.EXPAND, 5 )

        bSizer53 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer53.SetMinSize( wx.Size( -3,-3 ) )
        self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, _(u"Calories Range (g):"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText8.Wrap( -1 )

        bSizer53.Add( self.m_staticText8, 0, wx.ALL, 5 )

        self.m_textCtrl11 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer53.Add( self.m_textCtrl11, 0, wx.ALL, 5 )

        self.m_textCtrl12 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer53.Add( self.m_textCtrl12, 0, wx.ALL, 5 )


        gSizer2.Add( bSizer53, 1, wx.EXPAND, 5 )

        self.m_button1 = wx.Button( self, wx.ID_ANY, _(u"Search"), wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer2.Add( self.m_button1, 0, wx.ALL, 5 )

        self.m_button2 = wx.Button( self, wx.ID_ANY, _(u"Reset"), wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer2.Add( self.m_button2, 0, wx.ALL, 5 )

        self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, _(u"Results"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText9.Wrap( -1 )

        gSizer2.Add( self.m_staticText9, 0, wx.ALL, 5 )

        self.m_textCtrl13 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,300 ), wx.TE_MULTILINE )
        gSizer2.Add( self.m_textCtrl13, 0, wx.ALL, 5 )


        self.SetSizer( gSizer2 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_button1.Bind( wx.EVT_BUTTON, self.on_search )
        self.m_button2.Bind( wx.EVT_BUTTON, self.on_reset )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def on_search( self, event ):
        event.Skip()

    def on_reset( self, event ):
        event.Skip()


