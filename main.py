from bearing import *                                      # Импортируем все необходимое из пакетов


defaults_calc = {'Частота вращения вала, об/мин, n': 1444.5,      # Данные из таблицы 3.1
                 'Коэффициент безопасности, Кб': 1.3,             # "Исходные данные для расчёта
                 'Температура подшипникового узла, град.': 100,   # подшипников на долговечность"
                 'Температурный коэффициент, КТ': 1,
                 'Режим работы': 'Средний равновероятный',        # Источник:
                 'Коэффициент эквивалентности': 0.25,             # Исходные_данные_для_расчета_
                 'Радиальная нагрузка  кН, Fr': 2.08,             # подшипника_на_долговечность_1_1.doc
                 'Осевая нагрузка, кН, Fa': 3.142,
                 'Динамическая грузоподъемность, кН, C': 15.7,
                 'Статическая грузоподъемность, кН, C0': 8.31,
                 'Параметр осевого нагружения, е': 0.21,
                 'Коэффициент радиальной нагрузки, X': 0.46,
                 'Коэффициент осевой нагрузки, Y': 1.421}

defaults_draw = {'d, мм': 20,                                     # Данные из таблицы 3.3
                 'D, мм': 47,                                     # "Подшипники шариковые радиально-упорные
                 'B, мм': 14,                                     # однорядные (ГОСТ 831-75)"
                 'r, мм': 1.5}                                    # Источник: Задача для курсовой работы.doc


def main():
    win = MyWin()
    win.customize()
    win.add_label_field('Начертить подшипник', (15, 10), 10)
    win.add_data_field('d', 'd', 'мм', (30, 50), 30)
    win.add_data_field('D', 'D', 'мм', (30, 80), 30)
    win.add_data_field('B', 'B', 'мм', (30, 110), 30)
    win.add_data_field('r', 'r', 'мм', (30, 140), 30)
    win()


if __name__ == '__main__':
    main()
