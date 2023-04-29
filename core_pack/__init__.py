import tkinter as tk


class Core:
    """Класс для инициализации ядра окна.
    Необходимые поля добавляются в рамках паттерна проектирования Mixins"""
    def __init__(self):
        self.main_win = tk.Tk()