# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
#
# Для определения расхода ткани по каждому типу одежды использовать формулы:
#                                                                   для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
# Проверить работу этих методов на реальных данных.
#
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:
#        реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

# class Clothes:
from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, size):
        self.size = size

    @abstractmethod
    def textile(self):
        pass

    def __add__(self, other):
        return 'Общее количество необходимой ткани: ' + str(self.textile() + other.textile()) + ' м'

class Coat(Clothes):
    def textile(self):
        return (self.size / 6.5 + 0.5)

class Costume(Clothes):
    def textile(self):
        return (2 * self.size + 0.3)

coat_1 = Coat(13)
costume_1 = Costume(6)
print('Ткань для пальто: ', coat_1.textile(), 'м Ткань для костюма: ', costume_1.textile(), ' м')
print(coat_1 + costume_1)