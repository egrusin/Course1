from bearing import *                                      # Импортируем все необходимое из пакетов


defaults_calc = {'C': 15.7,                            # Данные из таблицы 3.1
                 'p': 3,                                   # "Исходные данные для расчёта
                 'Fr': 2.08,                           # подшипников на долговечность"
                 'Fa': 3.142,                          # Источник:
                 'X': 0.46,                                # Исходные_данные_для_расчета_
                 'Y': 1.421,                               # подшипника_на_долговечность_1_1.doc
                 'V': 1,
                 'k_b': 1.3,
                 'k_t': 1}

defaults_draw = {'d': 20,                              # Данные из таблицы 3.3
                 'D': 47,                              # "Подшипники шариковые радиально-упорные
                 'B': 14,                              # однорядные (ГОСТ 831-75)"
                 'r': 1.5}                             # Источник: Задача для курсовой работы.doc


def main(draw_data, calc_data):
    data = DrawData(draw_data)
    calc = CalcData(calc_data)

    win = MyWin(data, calc)
    draw_plases(win)

    image = get_image('images/goal.png')
    get_window(win, data, image)
    win()


if __name__ == '__main__':
    main(defaults_draw, defaults_calc)
