from tkinter import *
from sub_frames.loginFrame import LoginFrame


class MainFrame(Frame):
    def __init__(self, master, **kwargs):
        super(MainFrame, self).__init__(master, **kwargs)
        self.widget(master)

    def widget(self, master):
        login_frame = LoginFrame(master)
        login_frame.pack()
        pass
