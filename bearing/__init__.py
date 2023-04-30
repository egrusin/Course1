from .core import *
from .calculate import *


class MyWin(ButtonWin, LabelWin, CustomWin, DrawWin):
    pass


def draw_plases(win, coords: DrawCoords):
    win.draw_rect(5, 5, 395, 595)
    win.draw_rect(405, 5, 795, 595)


def get_window(win):
    win.customize('Расчет подшипника на долговечность', (1200, 600))

    win.add_label_field('Начертить подшипник', (15, 10), 10)
    win.add_data_field('d', 'd', 'мм', (30, 50), 30)
    win.add_data_field('D', 'D', 'мм', (30, 80), 30)
    win.add_data_field('B', 'B', 'мм', (30, 110), 30)
    win.add_data_field('r', 'r', 'мм', (30, 140), 30)

    win.add_button('Значения по умолчанию', win.set_data, (10, 350), 20)
    win.add_button('Начертить подшипник', lambda: print(win.data.data), (10, 380), 20)

    win.add_label_field('Рассчитать подшипник', (200, 10), 10)
    win.add_calc_field('C', 'C', ', кН', (220, 50), 30)
    win.add_calc_field('p', 'p', '', (220, 80), 30)
    win.add_calc_field('Fr', 'Fr', ', кН', (220, 110), 30)
    win.add_calc_field('Fa', 'Fa', ', кН', (220, 140), 30)
    win.add_calc_field('X', 'X', '', (220, 170), 30)
    win.add_calc_field('Y', 'Y', '', (220, 200), 30)
    win.add_calc_field('V', 'V', '', (220, 230), 30)
    win.add_calc_field('k_b', 'Kb', '', (220, 260), 30)
    win.add_calc_field('k_t', 'KT', '', (220, 290), 30)

    win.add_button('Значения по умолчанию', win.set_calc, (200, 350), 20)
    win.add_button('Рассчитать подшипник', win.get_calc, (200, 380), 20)
    win.add_answer_field('P', 'P', ', кН', (220, 410), 30)
    win.add_answer_field('L', 'L', ', млн об.', (220, 440), 30)





