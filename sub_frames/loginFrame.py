from tkinter import *


class LoginFrame(Frame):
    def __init__(self, master: Tk, **kwargs):
        super(LoginFrame, self).__init__(master, **kwargs)
        w, h = 500, 300
        screen_w, screen_h = master.winfo_screenwidth(), master.winfo_screenheight()
        place = (w, h, int((screen_w - w) / 2), int((screen_h - h) / 2))
        master.geometry("{}x{}+{}+{}".format(*place))
        self.widget()

    def widget(self):
        row = 0
        column = 0
        self.config(bg="red")
        Label(self, text="RunYinCorporation", font=("黑体", 18), fg="purple").grid(row=row, column=column)

