from .core import *
from .calculate import *


class MyWin(ButtonWin, LabelWin, CustomWin, DrawWin):
    pass


def draw_plases(win) -> None:
    win.draw_rect(5, 5, 395, 595)
    win.draw_rect(405, 5, 795, 595)


def create_draw(win: MyWin, data):
    def inner():
        left_angle = (5, 5)
        size = (390, 590)
        for k in win.entries_draw:
            data[k] = float(win.entries_draw.get(k).get())

        coords = DrawCoords(data, left_angle, size)
        coords.resize_data()
        coords.add_params()
        center = coords.get_center()
        # Очищаем место
        win.clear_place(5, 5, 395, 595)
        # Рисуем внешний контур
        out_fig = coords.get_outer_polygon()
        win.draw_line(*(out_fig + out_fig[:2]), size=3)
        # Рисуем осевую линию
        win.draw_line(center[0] - 3, center[1], center[0] + 4, center[1], size=1)
        win.draw_line(center[0], center[1] - 4, center[0], center[1] + 4, size=1)
        win.draw_line(center[0] - 20 - coords['B'] // 2, center[1], center[0] - 5, center[1], size=1)
        win.draw_line(center[0] + 6, center[1], center[0] + 20 + coords['B'] // 2, center[1], size=1)
        # Рисуем внутренний цилиндр
        in_cil = coords.get_inner_cilinder()
        win.draw_line(*(in_cil + in_cil[:2]), size=3)
        # Рисуем косые
        win.draw_line(in_cil[0] - coords['r'], in_cil[1] - coords['r'], in_cil[0], in_cil[1], size=3)
        win.draw_line(in_cil[2] + coords['r'], in_cil[3] - coords['r'], in_cil[2] , in_cil[3], size=3)
        win.draw_line(in_cil[4] + coords['r'], in_cil[5] + coords['r'], in_cil[4], in_cil[5], size=3)
        win.draw_line(in_cil[6] - coords['r'], in_cil[7] + coords['r'], in_cil[6], in_cil[7], size=3)
        # Рисуем цилиндр до шариков, статор
        big_cil = coords.get_big_cilinder()
        win.draw_line(*(big_cil + big_cil[:2]), size=3)
        # Штрихуем статор
        up_in_fill = coords.fill_up_stator()      # Верхняя часть
        for i in up_in_fill:
            win.draw_line(*i, size=1)
        down_in_fill = coords.fill_down_stator()  # Нижняя часть
        for i in down_in_fill:
            win.draw_line(*i, size=1)
        # Рисуем внутреннюю для подшипника сторону
        up_lines = coords.get_upinner_lines()
        win.draw_line(*up_lines[:4], size=3)
        win.draw_line(*up_lines[4:], size=3)
        down_lines = coords.get_downinner_lines()
        win.draw_line(*down_lines[:4], size=3)
        win.draw_line(*down_lines[4:], size=3)
        # Штрихуем ротор
        up_out_fill = coords.fill_up_rotor()      # Верхняя часть
        for i in up_out_fill:
            win.draw_line(*i, size=1)
        down_out_fill = coords.fill_down_rotor()  # Нижняя часть
        for i in down_out_fill:
            win.draw_line(*i, size=1)
        # win.draw_polygon(*coords.get_ficha(), size=5)
        # Рисуем подшипники
        up_cir = coords.get_upcircle_params()
        win.draw_circle(*up_cir, size=3)
        down_cir = coords.get_downcircle_params()
        win.draw_circle(*down_cir, size=3)

    return inner


def get_window(win, data: DrawData):
    win.customize('Расчет подшипника на долговечность', (1200, 600))
    # Поля для черчения
    win.add_label_field('Начертить подшипник', (15, 10), 10)
    win.add_data_field('d', 'd', 'мм', (30, 50), 30)
    win.add_data_field('D', 'D', 'мм', (30, 80), 30)
    win.add_data_field('B', 'B', 'мм', (30, 110), 30)
    win.add_data_field('r', 'r', 'мм', (30, 140), 30)

    win.add_button('Значения по умолчанию', win.set_data, (10, 350), 20)
    win.add_button('Начертить подшипник', create_draw(win, data), (10, 380), 20)
    # Поля для расчета
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
