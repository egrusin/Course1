import window_pack
import drawing_pack  # Импортируем все пакеты


defaults_calc = {'Частота вращения вала, об/мин, n': 1444.5,      # Данные из таблицы 3.1
                 'Коэффициент безопасности, Кб': 1.3,             # "Исходные данные для расчёта
                 'Температура подшипникового узла, град.': 100,   # подшипников на долговечность"
                 'Температурный коэффициент, КТ': 1,
                 'Режим работы': 'Средний равновероятный',
                 'Коэффициент эквивалентности': 0.25,
                 'Радиальная нагрузка  кН, Fr': 2.08,
                 'Осевая нагрузка, кН, Fa': 3.142,
                 'Динамическая грузоподъемность, кН, C': 15.7,
                 'Статическая грузоподъемность, кН, C0': 8.31,
                 'Параметр осевого нагружения, е': 0.21,
                 'Коэффициент радиальной нагрузки, X': 0.46,
                 'Коэффициент осевой нагрузки, Y': 1.421}

defaults_draw = {'d, мм': 20,
                 'D, мм': 47,
                 'B, мм': 14,
                 'r, мм': 1.5}


def main():
    pass


if __name__ == '__main__':
    main()
