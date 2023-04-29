__all__ = ['DrawData', 'DrawCoords']


class DrawData:
    """Класс для рассчета недостающих параметров подшипника"""
    def __init__(self, data: dict) -> None:
        """Инициализатор данных класса
        :param data: dict - Словарь с имеющимися данными о подшипнике"""
        self.B = data.get('B, мм')
        self.D = data.get('D, мм')
        self.d = data.get('d, мм')
        self.r = data.get('r, мм')
        self.Dw = 0.32 * (self.D - self.d)
        self.S = 0.15 * (self.D - self.d)
        self.d1 = 0.5 * (self.D + self.d)

    def __mul__(self, other):
        self.B *= other
        self.D *= other
        self.d *= other
        self.r *= other
        self.Dw *= other
        self.S *= other
        self.d1 *= other


class DrawCoords:
    """Класс для рассчета координат ключевых точек чертежа"""
    def __init__(self, data: DrawData, field_coords: tuple, field_size: tuple) -> None:
        """Инициализируем размеры подшипника и поля для чертежа"""
        self.data = data
        self.field_coords = field_coords
        self.field_size = field_size

    def __call__(self, win) -> None:
        """Чертящий метод"""
                    # Находим центр чертежа
        draw_center = (self.field_coords[0] + self.field_size[0] // 2, self.field_coords[1] + self.field_size[1] // 2)
                    # Расчитываем коэффициент пропорциональности
        k = (self.field_size[0] - 100) // self.data.D
                    # Увеличиваем параметры подшипника
        self.data * k
                    # Отмечаем центр
        c1 = (draw_center[0] - 3, draw_center[1], draw_center[0] + 3, draw_center[1])
        win.draw_line(*c1)
        c2 = (draw_center[0], draw_center[1] - 3, draw_center[0], draw_center[0] + 3)
        win.draw_line(*c2)
