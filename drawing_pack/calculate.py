__all__ = ['DrawData']


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
