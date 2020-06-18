# 4. Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
#
class Warehouse:
    def __init__(self, products):
        self.products = products

class Office_eqiupment:
    def __init__(self, manufacturer, weight, quantity, price):
        self.weight = weight                # вес
        self.quantity = quantity            # количество
        self.price = price                  # цена
        self.manufacturer = manufacturer    # производитель

class Printer(Office_eqiupment):
    def __init__(self, type, manufacturer, weight, quantity, price):
        self.__type = type
        super().__init__(manufacturer, weight, quantity, price)
        print(f'Добавлени принтер {self.manufacturer}, тип {self.__type}, весом {self.weight} кг, в количестве {self.quantity} шт за {self.price} руб/шт')

class Scanner(Office_eqiupment):
    def __init__(self, color_render, manufacturer, weight, quantity, price):
        self.__color_render = color_render
        super().__init__(manufacturer, weight, quantity, price)
        print(f'Добавлени принтер {self.manufacturer}, цветопередача {self.__color_render}, весом {self.weight} кг, в количестве {self.quantity} шт за {self.price} руб/шт')


class Xerox(Office_eqiupment):
    def __init__(self, format, manufacturer, weight, quantity, price):
        self.__format = format
        super().__init__(manufacturer, weight, quantity, price)
        print(f'Добавлени принтер {self.manufacturer}, формат {self.__format}, весо {self.weight} кг, в количестве {self.quantity} шт за {self.price} руб/шт')

printer = Printer('лазерный', 'Canon', '5', '10', '5999')
scanner = Scanner('ч/б', 'Acer', '2', '7', '2499')
xerox = Xerox('А4', 'Citizen', '3', '5', '3590')