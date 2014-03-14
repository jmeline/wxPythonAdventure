__author__ = 'Jacob'

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#     First, Solve the problem. Then, write the code. -John Johnson     #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

## Make a simple Frame

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

app = wx.App(redirect=False)
frame = TestFrame(None, "Hello, World!")
frame.Show()
app.MainLoop()


