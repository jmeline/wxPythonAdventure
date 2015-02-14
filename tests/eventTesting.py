# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct  2 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class Frame
###########################################################################

class Frame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 210,203 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

        self.txt = wx.StaticText( self, wx.ID_ANY, u"Text", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txt.Wrap( -1 )

        self.txt2 = wx.StaticText( self, wx.ID_ANY, u"Text2", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txt2.Wrap( -1 )

        self.txt3 = wx.StaticText( self, wx.ID_ANY, u"text3", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txt3.Wrap( -1 )

        self.btn1 = wx.Button( self, wx.ID_ANY, u"Button1", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.btn2 = wx.Button( self, wx.ID_ANY, u"Button2", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.btn3 = wx.Button( self, wx.ID_ANY, u"Button3", wx.DefaultPosition, wx.DefaultSize, 0 )

        sb = wx.StaticBox( self, wx.ID_ANY, u"Labels" )
        sb2 = wx.StaticBox( self, wx.ID_ANY, u"Buttons" )

        sbLabels = wx.StaticBoxSizer( sb, wx.VERTICAL )
        sbLabels.Add( self.txt, 0, wx.ALL|wx.EXPAND, 5 )
        sbLabels.Add( self.txt2, 0, wx.ALL, 5 )
        sbLabels.Add( self.txt3, 0, wx.ALL, 5 )

        sbButtons = wx.StaticBoxSizer( sb2, wx.VERTICAL )
        sbButtons.Add( self.btn1, 0, wx.ALL|wx.EXPAND, 5 )
        sbButtons.Add( self.btn2, 0, wx.ALL, 5 )
        sbButtons.Add( self.btn3, 0, wx.ALL, 5 )

        #print dir(sbButtons.StaticBox)

        sb.Bind(wx.EVT_LEFT_UP, self.onTxtClicked)
        sb2.Bind(wx.EVT_LEFT_UP, self.onTxtClicked)

        fgMiddle = wx.FlexGridSizer( 0, 2, 0, 0 )
        fgMiddle.SetFlexibleDirection( wx.BOTH )
        fgMiddle.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        fgMiddle.Add( sbLabels, 0, wx.ALL|wx.EXPAND, 5 )
        fgMiddle.Add( sbButtons, 1, wx.EXPAND, 5 )

        bSizerMain = wx.BoxSizer( wx.HORIZONTAL )
        bSizerMain.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"label" ), wx.VERTICAL )
        sbSizer3.Add( fgMiddle, 1, wx.ALL|wx.EXPAND, 5 )
        bSizerMain.Add( sbSizer3, 1, wx.EXPAND, 5 )
        bSizerMain.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )

        self.SetSizer( bSizerMain )
        self.Layout()

        self.Centre( wx.BOTH )

        self.initEvents()

    def __del__( self ):
        pass

    def initEvents(self):

        self.txt.Bind(wx.EVT_LEFT_UP, self.onTxtClicked)
        self.txt2.Bind(wx.EVT_LEFT_UP, self.onTxt2Clicked)
        self.txt3.Bind(wx.EVT_LEFT_UP, self.onTxt3Clicked)
        self.btn1.Bind(wx.EVT_BUTTON, self.onBtnPressed)
        self.btn2.Bind(wx.EVT_BUTTON, self.onBtn2Pressed)
        self.btn3.Bind(wx.EVT_BUTTON, self.onBtn3Pressed)

    def onTxtClicked(self, evt):
        print evt

    def onTxt2Clicked(self, evt):
        print evt

    def onTxt3Clicked(self, evt):
        print evt

    def onBtnPressed(self, evt):
        print evt

    def onBtn2Pressed(self, evt):
        print evt

    def onBtn3Pressed(self, evt):
        print evt

app = wx.App()
frame = Frame(None)
frame.Show()
app.MainLoop()