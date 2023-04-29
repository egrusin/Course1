__all__ = ['CustomWin', 'LabelWin']


import tkinter as tk


class CoreWin:
    """Ядро главного окна. Подтягивает необходимые объекты из tkinter"""
    def __init__(self) -> None:
        self.main_win = tk.Tk()

    def __call__(self) -> None:
        self.main_win.mainloop()


class CustomWin(CoreWin):
    """Класс-кастомизатор главного окна. Добавляет название, размеры и иконку"""
    def customize(self, title='Расчет подшипника на долговечность') -> None:
        self.main_win.title(title)
        self.main_win.geometry('900x600+400+100')
        self.main_win.resizable(False, False)
        icon = tk.PhotoImage(file='images/icon.png')
        self.main_win.iconphoto(False, icon)


class LabelWin(CoreWin):
    """Класс для добавления в окно полей ввода и информационных подписей"""
    def __init__(self) -> None:
        super().__init__()
        self.entries = {}

    def add_data_field(self, entry_name, label_start, label_end, position, dx) -> None:
        """Метод для добавления в окно поля вида F = |0.034  |, мм"""
        tk.Label(self.main_win, text=f'{label_start} =').place(x=position[0], y=position[1])
        entry = tk.Entry(self.main_win, width=7)
        entry.place(x=position[0] + dx, y=position[1])
        self.entries[entry_name] = entry
        tk.Label(self.main_win, text=f', {label_end}').place(x=position[0] + dx * 2.5, y=position[1])

    def add_label_field(self, label_text, position, size) -> None:
        tk.Label(self.main_win, text=f'{label_text}', font=('Arial', size)).place(x=position[0], y=position[1])




