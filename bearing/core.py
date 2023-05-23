__all__ = ['CustomWin', 'LabelWin', 'ButtonWin', 'DrawWin', 'get_image']


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
        self.entries_calc = {}
        self.answers = {}

    def add_data_field(self, entry_name: str, label_start: str, label_end: str, position: tuple, dx: int) -> None:
        """Метод для добавления в окно поля вида F = |0.034  |, мм"""
        tk.Label(self.main_win, text=f'{label_start} =').place(x=position[0], y=position[1])
        entry = tk.Entry(self.main_win, width=6)
        entry.place(x=position[0] + dx, y=position[1])
        self.entries_draw[entry_name] = entry
        tk.Label(self.main_win, text=f', {label_end}').place(x=position[0] + dx * 2.5, y=position[1])

    def add_calc_field(self, entry_name: str, label_start: str, label_end: str, position: tuple, dx: int) -> None:
        """Метод для добавления в окно поля вида F = |0.034  |, мм"""
        tk.Label(self.main_win, text=f'{label_start} =').place(x=position[0], y=position[1])
        entry = tk.Entry(self.main_win, width=6)
        entry.place(x=position[0] + dx, y=position[1])
        self.entries_calc[entry_name] = entry
        tk.Label(self.main_win, text=f'{label_end}').place(x=position[0] + dx * 2.5, y=position[1])

    def add_answer_field(self, entry_name: str, label_start: str, label_end: str, position: tuple, dx: int) -> None:
        """Метод для добавления в окно поля вида F = |0.034  |, мм"""
        tk.Label(self.main_win, text=f'{label_start} =').place(x=position[0], y=position[1])
        entry = tk.Entry(self.main_win, width=9)
        entry.place(x=position[0] + dx, y=position[1])
        self.answers[entry_name] = entry
        tk.Label(self.main_win, text=f'{label_end}').place(x=position[0] + dx * 3, y=position[1])

    def add_label_field(self, label_text: str, position: tuple, size: int) -> None:
        """Метод для добавления в окно поля вида 'Начертить подшипник'"""
        tk.Label(self.main_win, text=f'{label_text}', font=('Arial', size)).place(x=position[0], y=position[1])


class ButtonWin(CoreWin):
    """Класс для добавления в окно именованных кнопок"""
    def __init__(self, data, calc):
        super().__init__()
        self.data = data
        self.calc = calc

    def add_button(self, but_text: str, but_func, position: tuple, size: int) -> None:
        """Метод для добавления в окно кнопки вида |Начертить подшипник|"""
        tk.Button(self.main_win, text=f'{but_text}', command=but_func, width=size).place(x=position[0], y=position[1])

    def set_data(self) -> None:
        """Метод для подстановки в окна значений по умолчанию из переменной data. Перед постановкой данные удаляются"""
        for i in self.entries_draw:
            self.entries_draw.get(i).delete(0, tk.END)
            value = self.data.base_data.get(i)
            self.entries_draw[i].insert(-1, value)
            self.data[i] = value

    def set_calc(self) -> None:
        """Метод для подстановки в окна значений по умолчанию из переменной calc. Перед постановкой данные удаляются"""
        for i in self.entries_calc:
            self.entries_calc.get(i).delete(0, tk.END)
            value = self.calc.base_data.get(i)
            self.entries_calc[i].insert(-1, value)
            self.calc[i] = value

    def get_calc(self) -> None:
        """Метод для подстановки в окна значений L и P по расчетам класса CalcData"""
        for i in self.entries_calc:
            val = self.entries_calc.get(i).get()
            self.calc[i] = val
        P = self.calc.get_P()
        self.answers.get('P').delete(0, tk.END)
        self.answers.get('P').insert(-1, P)
        L = self.calc.get_L()
        self.answers.get('L').delete(0, tk.END)
        self.answers.get('L').insert(-1, L)


class DrawWin(CoreWin):
    """Класс для рисования чертежа"""
    def __init__(self):
        super().__init__()
        self.canvas = tk.Canvas(bg="white", width=800, height=600)
        self.canvas.place(x=395, y=0)

    def draw_line(self, *args, size=1) -> None:
        """Метод для рисования ломаной линии толщины size по координатам args"""
        self.canvas.create_line(*args, width=size)

    def draw_rect(self, *args, size=1) -> None:
        """Метод для рисования прямоугольника толщины size по координатам args"""
        self.canvas.create_rectangle(*args, width=size)

    def draw_circle(self, *args, size=1) -> None:
        """Метод для рисования окружности толщины size по координатам args"""
        self.canvas.create_oval(*args, width=size, fill='white')

    def clear_place(self, *args, size=1):
        """Метод для удаления чертежа"""
        self.canvas.create_rectangle(*args, width=size, fill='white')

    def draw_polygon(self, *args, size=3, fill=True):
        """Метод для рисования окружности толщины size по координатам args"""
        self.canvas.create_polygon(*args, width=size, fill='white')

    def draw_3d(self, x, y, image):
        self.canvas.create_image(x, y, anchor='nw', image=image)

    def draw_punctir(self, *args, size=1) -> None:
        """Метод для рисования пунктирной линии толщины size по координатам args"""
        self.canvas.create_line(*args, width=size, dash=5)


def get_image(path):
    return tk.PhotoImage(file=path, height=590, width=390)
