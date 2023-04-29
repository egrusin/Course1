__all__ = ['CustomWin']

import tkinter as tk


class CoreWin:
    def __init__(self):
        self.main_win = tk.Tk()

    def __call__(self):
        self.main_win.mainloop()


class CustomWin(CoreWin):
    def customize(self, title='Расчет подшипника на долговечность'):
        self.main_win.title(title)
        self.main_win.geometry('800x500')
        self.main_win.resizable(False, False)
        icon = tk.PhotoImage(file='images/icon.png')
        self.main_win.iconphoto(False, icon)
