import wx



class my_gui(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(my_gui, self).__init__(*args, **kwargs)

        self.SetSize((500, 500))
        self.Centre()
        self.Crazy()
        self.Show()
        

    def Crazy(self):

        panel = wx.Panel(self)
        menu = wx.MenuBar()
        self.col = wx.Colour(0, 0, 0)

        
        
        font = wx.Font(12, wx.DECORATIVE, wx.SLANT, wx.BOLD)
        heading = wx.StaticText(panel, label= 'Color Picker', pos = (190, 20))
        heading.SetFont(font)
        wx.StaticLine(panel, pos = (100, 50), size = (300, 1))
        wx.StaticBox(panel, label = 'Choose your color', pos = (10, 80), size = (170, 120))

        rb1 = wx.ToggleButton(panel, label = 'Red', pos = (15, 100), style = wx.RB_GROUP)
        rb2 = wx.ToggleButton(panel, label = 'Blue', pos = (15, 130))
        rb3 = wx.ToggleButton(panel, label = 'Green', pos = (15, 160))

        self.cpanel = wx.Panel(panel, pos = (220, 80), size = (120, 120))
        self.cpanel.SetBackgroundColour(self.col)

        rb1.Bind(wx.EVT_TOGGLEBUTTON, self.ToggleRed)
        rb2.Bind(wx.EVT_TOGGLEBUTTON, self.ToggleBlue)
        rb3.Bind(wx.EVT_TOGGLEBUTTON, self.ToggleGreen)

       
        

        fileButton = wx.Menu()
        editButton = wx.Menu()
        exitItem = wx.MenuItem(fileButton, wx.ID_EXIT, 'Exit')
        openItem = wx.MenuItem(fileButton, wx.ID_OPEN, 'Open')
        undoItem = wx.MenuItem(editButton, wx.ID_UNDO, 'Undo')
        redoItem = wx.MenuItem(editButton, wx.ID_REDO, 'Redo')
        fileButton.AppendItem(exitItem)
        fileButton.AppendItem(openItem)
        editButton.AppendItem(undoItem)
        editButton.AppendItem(redoItem)

        menu.Append(fileButton, 'File')
        menu.Append(editButton, 'Edit')

        self.SetMenuBar(menu)
        self.Bind(wx.EVT_MENU, self.close, exitItem)

    def ToggleRed(self, e):
        obj = e.GetEventObject()
        chosen = obj.GetValue()
        
        green = self.col.Green()
        blue = self.col.Blue()
        

        if chosen:
            self.col.Set(255, green, blue)
        else:
            self.col.Set(0, green, blue)

        self.cpanel.SetBackgroundColour(self.col)
        self.cpanel.Refresh()

    def ToggleBlue(self, e):
        obj = e.GetEventObject()
        chosen = obj.GetValue()

        red = self.col.Red()
        green = self.col.Green()

        if chosen:
            self.col.Set(red, green, 255)
        else:
            self.col.Set(red, green, 0)

        self.cpanel.SetBackgroundColour(self.col)
        self.cpanel.Refresh()

    def ToggleGreen(self, e):
        obj = e.GetEventObject()
        chosen = obj.GetValue()

        red = self.col.Red()
        blue = self.col.Blue()

        if chosen:
            self.col.Set(red, 255, blue)
        else:
            self.col.Set(red, 0, blue)

        self.cpanel.SetBackgroundColour(self.col)
        self.cpanel.Refresh()
        

    def close(self,e):
        self.Close(True)

        
def Main():
        app = wx.App()
        my_gui(None, title = "My Window")

        app.MainLoop()


if __name__ == '__main__':
    Main()
