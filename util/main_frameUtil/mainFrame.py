from tkinter import *
from util.other_frameUtil.loginFrame import LoginFrame


class MainFrame(Frame):
    def __init__(self, master, **kwargs):
        super(Frame, self).__init__(master, **kwargs)

        #  初始化变量

        self.widget()

    def widget(self):
        login_frame = LoginFrame(self)
        login_frame.pack()

