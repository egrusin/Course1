__all__ = ['DrawData', 'DrawCoords', 'CalcData']


class DrawData:
    """Класс для рассчета недостающих параметров подшипника"""
    def __init__(self, data: dict) -> None:
        """Инициализатор данных класса
        :param data: dict - Словарь с имеющимися данными о подшипнике"""
        self.base_data = data
        self.data = dict.fromkeys(self.base_data, 0)
        self.Dw = 0.32 * (self.data['D'] - self.data['d'])
        self.S = 0.15 * (self.data['D'] - self.data['d'])
        self.d1 = 0.5 * (self.data['D'] + self.data['d'])

    def __mul__(self, other):
        for i in self.data:
            self.data[i] *= 2

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
        X = float(self.data.get('X'))
        V = float(self.data.get('V'))
        Fr = float(self.data.get('Fr'))
        Y = float(self.data.get('Y'))
        Fa = float(self.data.get('Fa'))
        Kb = float(self.data.get('k_t'))
        KT = float(self.data.get('k_t'))
        return round((X * V * Fr + Y * Fa) * Kb * KT, 4)

    def get_L(self):
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
    def __init__(self, data: DrawData, field_coords: tuple=(405, 5), field_size: tuple=(390, 590)) -> None:
        """Инициализируем размеры подшипника и поля для чертежа"""
        self.data = data
        self.field_coords = field_coords
        self.field_size = field_size

    def resize_data(self):
        """Метод для пропорционального увеличения параметров data"""
        k = (self.field_size[0] - 100) // self.data['D']
        self.data * k

    def get_center(self):
        return self.field_coords[0] + self.field_size[0] // 2, self.field_coords[1] + self.field_size[1] // 2

    def __call__(self) -> None:
        pass

