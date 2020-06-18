# 5. Продолжить работу над первым заданием.
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
#                                                       можно использовать любую подходящую структуру, например словарь.

class Warehouse:
    def __init__(self, products):
        self.products = products

class Office_eqiupment:
    def __init__(self, manufacturer, weight, quantity, price):
        self.information = {}
        self.weight = weight                # вес
        self.quantity = quantity            # количество
        self.price = price                  # цена
        self.manufacturer = manufacturer    # производитель

    def ad_product(self, other):
        print('На склад поступил новый товар: ', self.information)
        other.products = str(int(other.products) + 1)
        print('Количество товаров на складе: ', other.products)

    def sending(self, other, company):
        print(f'Товар отправлен в компанию {company}')
        other.products = str(int(other.products) - 1)
        print('Количество товаров на складе: ', other.products)

class Printer(Office_eqiupment):
    def __init__(self, type, manufacturer, weight, quantity, price):
        self.__type = type
        super().__init__(manufacturer, weight, quantity, price)
        self.information = {'Вид': 'Printer', 'Производитель': self.manufacturer, 'Вес': self.weight, 'Кол-во': self.quantity, 'Цена': self.price}
        print(f'Добавлен принтер {self.manufacturer}, тип {self.__type}, весом {self.weight} кг, в количестве {self.quantity} шт за {self.price} руб/шт')

class Scanner(Office_eqiupment):
    def __init__(self, color_render, manufacturer, weight, quantity, price):
        self.__color_render = color_render
        super().__init__(manufacturer, weight, quantity, price)
        self.information = {'Вид': 'Scanner', 'Производитель': self.manufacturer, 'Вес': self.weight, 'Кол-во': self.quantity, 'Цена': self.price}
        print(f'Добавлен принтер {self.manufacturer}, цветопередача {self.__color_render}, весом {self.weight} кг, в количестве {self.quantity} шт за {self.price} руб/шт')


class Xerox(Office_eqiupment):
    def __init__(self, format, manufacturer, weight, quantity, price):
        self.__format = format
        super().__init__(manufacturer, weight, quantity, price)
        self.information = {'Вид': 'Xerox', 'Производитель': self.manufacturer, 'Размер': self.weight, 'Кол-во': self.quantity, 'Цена': self.price}
        print(f'Добавлен принтер {self.manufacturer}, формат {self.__format}, весом {self.weight} кг, в количестве {self.quantity} шт за {self.price} руб/шт')


wh = Warehouse('0') #создаем склад, где будет хранить товар
printer = Printer('Цифровой', 'Canon', '5', '10', '5999')
scanner = Scanner('есть', 'Acer', '2', '7', '2499')
xerox = Xerox('А4', 'Citizen', '2,5', '5', '3590')
xerox.ad_product(wh) # добавляем товар на этод склад
scanner.ad_product(wh)
printer.ad_product(wh)
scanner.sending(wh, 'ОАО Газпром') #отправляем товар с этого склада в компанию