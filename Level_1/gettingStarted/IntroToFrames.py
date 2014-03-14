__author__ = 'Jacob'

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#     First, Solve the problem. Then, write the code. -John Johnson     #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

## Make a simple Frame with a widget and status bar
import wx

class TestFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(300, 200))
        #test = wx.StaticText(self, label="Hello World!")

        ## Example of using a splitter
        self.sp = wx.SplitterWindow(self)
        self.p1 = wx.Panel(self.sp, style=wx.SUNKEN_BORDER)
        self.p2 = wx.Panel(self.sp, style=wx.SUNKEN_BORDER)
        self.sp.SplitVertically(self.p1, self.p2, 150)

        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetStatusText("Hola")

        self.siButton = wx.Button(self.p1, -1, "Si", size=(40, 20), pos=(10, 10))
        self.siButton.Bind(wx.EVT_BUTTON, self.Si)

        self.noButton = wx.Button(self.p2, -1, "No", size=(40, 20), pos=(10, 10))
        self.noButton.Bind(wx.EVT_BUTTON, self.No)

    def Si(self, evt):
        self.statusbar.SetStatusText("Si")

    def No(self, evt):
        self.statusbar.SetStatusText("No")


app = wx.App(redirect=False)
frame = TestFrame(None, "Hello, World!")
frame.Show()
app.MainLoop()


