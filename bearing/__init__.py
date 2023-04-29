from .core import *
from .calculate import *


class MyWin(ButtonWin, CustomWin, LabelWin, DrawWin):
    pass


def get_window(data):
    data = DrawData(data)
    draw_obj = DrawCoords(data, (405, 5), (390, 590))
    win = MyWin()
    win.customize('Расчет подшипника на долговечность', (1200, 600))
    win.add_label_field('Начертить подшипник', (15, 10), 10)
    win.add_data_field('d', 'd', 'мм', (30, 50), 30)
    win.add_data_field('D', 'D', 'мм', (30, 80), 30)
    win.add_data_field('B', 'B', 'мм', (30, 110), 30)
    win.add_data_field('r', 'r', 'мм', (30, 140), 30)
    win.add_button('Значения по умолчанию', win.set_data(data, win.entries_draw), (10, 300), 20)
    win.add_button('Начертить подшипник', win.draw_with(draw_obj), (10, 330), 20)
    return win



