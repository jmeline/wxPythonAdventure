__author__ = 'Jacob'

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#     First, Solve the problem. Then, write the code. -John Johnson     #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

## Make a simple Frame with a widget and status bar with Matplotlib
import wx
import numpy
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas


class TestFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(900, 600))
        #test = wx.StaticText(self, label="Hello World!")

        ## Example of using a splitter
        self.sp = wx.SplitterWindow(self)
        self.p1 = wx.Panel(self.sp, style=wx.SUNKEN_BORDER)
        self.p2 = wx.Panel(self.sp, style=wx.SUNKEN_BORDER)
        self.sp.SplitVertically(self.p1, self.p2, 800)

        ## Build Statusbar
        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetStatusText("Hola")

        ## Create Buttons
        self.yesButton = wx.Button(self.p2, -1, "Yes", size=(40, 20), pos=(10, 10))
        self.yesButton.Bind(wx.EVT_BUTTON, self.Yes)

        self.noButton = wx.Button(self.p2, -1, "No", size=(40, 20), pos=(10, 40))
        self.noButton.Bind(wx.EVT_BUTTON, self.No)

        self.figure = matplotlib.figure.Figure()
        self.axes = self.figure.add_subplot(111)
        x = numpy.arange(0.0,10,1.0)
        y = [0,1,1.7,3,4.1,5.2,6,6.7,7.5,9.2]
        self.axes.plot(x,y,'o--')
        self.canvas = FigureCanvas(self.p1, -1, self.figure)

    def Yes(self, evt):
        self.statusbar.SetStatusText("Yes!")

    def No(self, evt):
        self.statusbar.SetStatusText("No")

app = wx.App(redirect=False)
frame = TestFrame(None, "Hello, World!")
frame.Show()
app.MainLoop()


