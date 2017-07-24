import tkinter


class ColorPicker:
    """A color picker GUI"""
    def __init__(self, master):
        self.master = master
        self.frame = tkinter.Frame(master, borderwidth=10)
        self.frame.pack()

        # Red, green, and blue scales, colored respectively, and
        # associated variables, stored in a dictionary for later use.
        self.rgb = {}
        for name in ('red', 'green', 'blue'):
            self.rgb[name] = tkinter.IntVar()
            self.scale = tkinter.Scale(
                self.frame, orient='horizontal', from_=0, to_=255,
                resolution=1, length=400, bg=name,
                variable=self.rgb[name], command=lambda val: self.update())
            self.scale.pack()

        # Widgets that display the color and its hexadecimal representation.
        self.display = tkinter.Label(self.frame, bg='#000', width=57, height=3)
        self.display.pack()
        self.hex = tkinter.Label(self.frame, text='#000000')
        self.hex.pack()

    def update(self):
        new_color = '#'
        for name in ('red', 'green', 'blue'):
            # Append a two-character hex value to the hex color code string
            new_color += hex(self.rgb[name].get())[2:].zfill(2)
        self.display.config(bg=new_color)
        self.hex.config(text=new_color)

if __name__ == '__main__':
    window = tkinter.Tk()
    app = ColorPicker(window)
    window.mainloop()
