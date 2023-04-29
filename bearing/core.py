__all__ = ['CustomWin', 'LabelWin', 'ButtonWin', 'DrawWin']


import tkinter as tk


class CoreWin:
    """Ядро главного окна. Подтягивает необходимые объекты из tkinter"""
    def __init__(self) -> None:
        self.main_win = tk.Tk()

    def __call__(self) -> None:
        self.main_win.mainloop()


class CustomWin(CoreWin):
    """Класс-кастомизатор главного окна. Добавляет название, размеры и иконку"""
    def customize(self, title: str, size) -> None:
        self.main_win.title(title)
        self.main_win.geometry(f'{size[0]}x{size[1]}+200+100')
        self.main_win.resizable(False, False)
        icon = tk.PhotoImage(file='images/icon.png')
        self.main_win.iconphoto(False, icon)


class LabelWin(CoreWin):
    """Класс для добавления в окно полей ввода и информационных подписей"""
    def __init__(self) -> None:
        super().__init__()
        self.entries_draw = {}
        self.answer = None

    def add_data_field(self, entry_name: str, label_start: str, label_end: str, position: tuple, dx: int) -> None:
        """Метод для добавления в окно поля вида F = |0.034  |, мм"""
        tk.Label(self.main_win, text=f'{label_start} =').place(x=position[0], y=position[1])
        entry = tk.Entry(self.main_win, width=6)
        entry.place(x=position[0] + dx, y=position[1])
        self.entries_draw[entry_name] = entry
        tk.Label(self.main_win, text=f', {label_end}').place(x=position[0] + dx * 2.5, y=position[1])

    def add_label_field(self, label_text: str, position: tuple, size: int) -> None:
        """Метод для добавления в окно поля вида 'Начертить подшипник'"""
        tk.Label(self.main_win, text=f'{label_text}', font=('Arial', size)).place(x=position[0], y=position[1])

    def add_answer_field(self, position: tuple, size: int) -> None:
        entry = tk.Entry(self.main_win, width=size)
        entry.place(x=position[0] + dx, y=position[1])
        self.answer = entry


class ButtonWin(CoreWin):
    """Класс для добавления в окно именованных кнопок"""
    def add_button(self, but_text: str, but_func, position: tuple, size: int) -> None:
        """Метод для добавления в окно кнопки вида |Начертить подшипник|"""
        tk.Button(self.main_win, text=f'{but_text}', command=but_func, width=size).place(x=position[0], y=position[1])

    def draw_with(self, draw_class) -> None:
        draw_class(self)

    def set_data(self, data, fields: dict) -> None:
        """Переписать для variable"""                           # !!!!
        for i in fields:
            fields.get(i).insert(-1, getattr(data, i))


class DrawWin(CoreWin):
    """Класс для рисования чертежа"""
    def draw_line(self, *args, size: int=2) -> None:
        """Метод для рисования ломаной линии толщины size по координатам args"""
        canvas = tk.Canvas(self.main_win)
        canvas.create_line(*args, width=size)
