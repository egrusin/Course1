__all__ = ['CustomWin', 'LabelWin']


import tkinter as tk


class CoreWin:
    """Ядро главного окна. Подтягивает необходимые объекты из tkinter"""
    def __init__(self):
        self.main_win = tk.Tk()

    def __call__(self):
        self.main_win.mainloop()


class CustomWin(CoreWin):
    """Класс-кастомизатор главного окна. Добавляет название, размеры и иконку"""
    def customize(self, title='Расчет подшипника на долговечность'):
        self.main_win.title(title)
        self.main_win.geometry('800x500')
        self.main_win.resizable(False, False)
        icon = tk.PhotoImage(file='images/icon.png')
        self.main_win.iconphoto(False, icon)


class LabelWin(CoreWin):
    """Класс для добавления в окно поля вида F = |0.034  |, мм"""
    def add_label(self, label_text, position):
        label = tk.Label(self.main_win,
                         text=label_text)
        label.place(x=position[0], y=position[1])


