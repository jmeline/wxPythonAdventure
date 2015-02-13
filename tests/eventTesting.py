import wx

class Frame(wx.Frame):
    def __init__(self, parent, **kwargs):
        wx.Frame.__init__(self, parent, **kwargs)


app = wx.App()
frame = Frame(None)
frame.Show()
app.MainLoop()