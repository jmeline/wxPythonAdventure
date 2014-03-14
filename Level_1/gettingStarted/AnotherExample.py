
# http://www.science-emergence.com/WxpythonTutorial/MatplotlibAndWXpython/
# Highly recommend going to this site. Credit goes to them who wrote this program

import wx

import numpy

from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas


class TestFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(500, 500))

        self.create_main_panel()
        self.draw_figure()

    def create_main_panel(self):
        self.panel = wx.Panel(self)
        #wx.StaticText(self.panel,-1,"This is static text",(500,500))
        #basicText = wx.TextCtrl(self.panel, -1, "Hello !", pos=(300,300), size=(175, -1))
        self.data = [0, 0, 1, 3, 5, 7, 10, 15, 17, 14, 9, 5, 4, 1, 1, 0]
        self.textbox = wx.TextCtrl(self.panel, pos=(100, 430), size=(300, -1), style=wx.TE_PROCESS_ENTER)
        self.textbox.SetValue(' '.join(map(str, self.data)))
        #print self.textbox.GetValue()
        self.Bind(wx.EVT_TEXT_ENTER, self.on_text_enter, self.textbox)
        button = wx.Button(self.panel, label="Draw", pos=(10, 430))
        self.Bind(wx.EVT_BUTTON, self.on_draw_button, button)
        self.dpi = 100
        self.fig = Figure((5.0, 4.0), dpi=self.dpi)
        self.canvas = FigureCanvas(self.panel, -1, self.fig)
        self.axes = self.fig.add_subplot(111)

    def on_text_enter(self, event):
        self.draw_figure()

    def draw_figure(self):
        str = self.textbox.GetValue()
        #print 'hello 1', str
        #print map(int, str.split())
        self.data = map(int, str.split())
        #print 'self.data', self.data
        #self.figure = matplotlib.figure.Figure((5.0, 4.0))
        #self.axes = self.figure.add_subplot(111)
        x = numpy.arange(len(self.data))
        y = self.data
        self.axes.clear()
        self.axes.bar(x, y, width=1.0, bottom=0, color='Green', alpha=0.65, label='Legend')
        #self.canvas = FigureCanvas(self, -1, self.figure)
        self.canvas.draw()

    def on_draw_button(self, event):
        self.draw_figure()


if __name__ == "__main__":
    app = wx.App(redirect=False)
    frame = TestFrame(None, "Hello Matplotlib !")
    frame.Show()
    app.MainLoop()