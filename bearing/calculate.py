__all__ = ['DrawData', 'DrawCoords', 'CalcData']


class DrawData:
    """Класс для рассчета недостающих параметров подшипника"""
    def __init__(self, data: dict) -> None:
        """Инициализатор данных класса
        :param data: dict - Словарь с имеющимися данными о подшипнике"""
        self.base_data = data
        self.data = dict.fromkeys(self.base_data, 0)

    def __mul__(self, other):
        """Метод для пропорционального увеличения параметров подшипника"""
        for i in self.data:
            self.data[i] *= other

    def __getitem__(self, item):
        return self.data[item]

    def __setitem__(self, key, value):
        self.data[key] = float(value)


class CalcData:
    """Класс для расчета долговечности подшипника"""
    def __init__(self, data: dict) -> None:
        self.base_data = data
        self.data = dict.fromkeys(self.base_data, 0)

    def get_P(self):
        """Метод для расчета динамической нагрузки"""
        X = float(self.data.get('X'))
        V = float(self.data.get('V'))
        Fr = float(self.data.get('Fr'))
        Y = float(self.data.get('Y'))
        Fa = float(self.data.get('Fa'))
        Kb = float(self.data.get('k_t'))
        KT = float(self.data.get('k_t'))
        return round((X * V * Fr + Y * Fa) * Kb * KT, 4)

    def get_L(self):
        """Метод для расчета долговечности"""
        C = float(self.data.get('C'))
        p = float(self.data.get('p'))
        P = float(self.get_P())
        return round((C / P) ** p, 6)

    def __getitem__(self, item):
        return self.data[item]

    def __setitem__(self, key, value):
        self.data[key] = value


class DrawCoords:
    """Класс для рассчета координат ключевых точек чертежа"""
    def __init__(self, data: DrawData, field_coords: tuple=(5, 5), field_size: tuple=(390, 590)) -> None:
        """Инициализируем размеры подшипника и поля для чертежа"""
        self.data = data
        self.field_coords = field_coords
        self.field_size = field_size

    def add_params(self):
        self['S'] = 0.15 * (self.data['D'] - self.data['d'])
        self['Dw'] = 0.32 * (self.data['D'] - self.data['d'])
        self['d1'] = 0.5 * (self.data['D'] + self.data['d'])

    def resize_data(self):
        """Метод для пропорционального увеличения параметров data"""
        k = min((self.field_size[0] - 20)// float(self.data['B']), (self.field_size[1] - 50) // float(self.data['D']))
        self.data * k

    def get_center(self):
        x = self.field_coords[0] + self.field_size[0] // 2
        y = self.field_coords[1] + self.field_size[1] // 2
        return x, y

    def get_inner_cilinder(self):
        cent = self.get_center()
        x1 = cent[0] - 0.5 * self['B'] + self['r']                   # Левый верхний
        y1 = cent[1] - self['d'] // 2
        x2 = cent[0] + 0.5 * self['B'] - self['r']                   # Правый верхний
        y2 = y1
        x3 = cent[0] + 0.5 * self['B'] - self['r']                   # Правый нижний
        y3 = cent[1] + (self['d'] - self['d'] // 2)
        x4 = x1                                                      # Левый нижний
        y4 = y3
        return x1, y1, x2, y2, x3, y3, x4, y4

    def get_big_cilinder(self):
        cent = self.get_center()
        x1 = cent[0] - 0.5 * self['B']                               # Левый верхний
        y1 = cent[1] - self['d'] // 2 - self['S']
        x2 = cent[0] + 0.5 * self['B']                               # Правый верхний
        y2 = y1
        x3 = cent[0] + 0.5 * self['B']                               # Правый нижний
        y3 = cent[1] + (self['d'] - self['d'] // 2) + self['S']
        x4 = x1                                                      # Левый нижний
        y4 = y3
        return x1, y1, x2, y2, x3, y3, x4, y4

    def get_outer_polygon(self):
        cent = self.get_center()
        x1 = cent[0] - 0.5 * self['B'] + self['r']                          # Левый верхний
        y1 = cent[1] - self['D'] // 2
        x2 = cent[0] + 0.5 * self['B'] - self['r']                          # Правый верхний
        y2 = y1
        x3 = cent[0] + 0.5 * self['B']                                      # Правый нижний
        y3 = y1 + self['r']
        x4 = x3                                                             # Левый нижний
        y4 = cent[1] + self['D'] // 2 - self['r']
        x5 = x2                                                             # Левый верхний
        y5 = cent[1] + self['D'] // 2
        x6 = x1                                                             # Правый верхний
        y6 = y5
        x7 = cent[0] - 0.5 * self['B']                                      # Правый нижний
        y7 = y4
        x8 = x7                                                             # Левый нижний
        y8 = y3
        return x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7, x8, y8

    def get_upinner_lines(self):
        cent = self.get_center()
        x1 = cent[0] - 0.5 * self['B']
        y1 = cent[1] - self['D'] // 2 + self['S']
        x2 = cent[0]
        y2 = y1
        x3 = cent[0] + 0.5 * self['B']
        y3 = cent[1] - self['D'] // 2 + 0.5 * self['S']
        x4 = cent[0] + 0.15 * self['B']
        y4 = cent[1] - 0.5 * self['d1'] - (self['Dw'] ** 2 / 4 - (0.15 * self['B']) ** 2) ** 0.5
        return x1, y1, x2, y2, x3, y3, x4, y4

    def get_downinner_lines(self):
        cent = self.get_center()
        x1 = cent[0] - 0.5 * self['B']
        y1 = cent[1] + self['D'] // 2 - self['S']
        x2 = cent[0]
        y2 = y1
        x3 = cent[0] + 0.5 * self['B']
        y3 = cent[1] + self['D'] // 2 - 0.5 * self['S']
        x4 = cent[0] + 0.15 * self['B']
        y4 = cent[1] + 0.5 * self['d1'] + (self['Dw'] ** 2 / 4 - (0.15 * self['B']) ** 2) ** 0.5
        return x1, y1, x2, y2, x3, y3, x4, y4

    def get_upcircle_params(self):
        cent = self.get_center()
        x = cent[0]
        y = cent[1] - 0.5 * self['d1']
        r = 0.5 * self['Dw']
        return x - r, y - r, x + r, y + r

    def get_downcircle_params(self):
        cent = self.get_center()
        x = cent[0]
        y = cent[1] + 0.5 * self['d1']
        r = 0.5 * self['Dw']
        return x - r, y - r, x + r, y + r

    def __getitem__(self, item):
        return float(self.data[item])

    def __setitem__(self, key, value):
        self.data[key] = float(value)



