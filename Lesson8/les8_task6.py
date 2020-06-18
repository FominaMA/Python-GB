# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
#
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
#                                                                                           изученных на уроках по ООП.

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

class TextError(ValueError):
    def __init__(self, text_error):
        self.text_error = text_error

wh = Warehouse('0') #создаем склад, где будет храниться товар
new_products = []
i = 0
while i > -1:
    try:
        type_product = input(f'Введите вид оргтехники {i+1} (Подсказка: printer или scanner или xerox), (Введите stop, если хотите закончить ввод оргтехники): ')
        manufacturer = input(f'Введите производителя данной оргтехники {i + 1}: ')
        if type_product != 'printer' and type_product != 'scanner' and type_product != 'xerox' and type_product != 'stop':
            print('Неопознанный тип оргтехники!')
            continue
        elif type_product == 'stop':
            break
        else:
            quantity = input(f'Введите количество данной оргтехники {i+1}: ')
            if ord(quantity[0]) > 58 or ord(quantity[0]) < 47:
                raise TextError("В количестве необходимо ввести число!")
            else:
                price = input(f'Введите цену данной оргтехники {i+1} в рублях: ')
                if ord(price[0]) > 58 or ord(price[0]) < 47:
                    raise TextError("В цене необходимо ввести число!")
                else:
                    size = input(f'Введите вес данной оргтехники {i + 1} в кг: ')
                    if ord(size[0]) > 58 or ord(size[0]) < 47:
                        raise TextError("В весе необходимо ввести число!")
            if type_product == 'printer':
                    type = input(f'Введите тип принтера (lazer, jet): ')
                    product = Printer(type, manufacturer, size, quantity, price)
                    new_products.append(product)
                    i += 1
            elif type_product == 'scanner':
                    color_render = input(f'Введите цветопередачу сканера (color, b/w): ')
                    product = Scanner(color_render, manufacturer, size, quantity, price)
                    new_products.append(product)
                    i += 1
            elif type_product == 'xerox':
                    format = input(f'Введите формат ксерокса (А3, А4, А5): ')
                    product = Xerox(format, manufacturer, size, quantity, price)
                    new_products.append(product)
                    i += 1
    except TextError as txt:
        print(txt)

print(new_products)

for i in range(len(new_products)):
    print(new_products[i].ad_product(wh)) # Добавляем созданный товар на склад

# Чтобы было проще, можете ввести:
# вид:                              printer             scanner         xerox
# производитель                     Canon               Asus            Epson
# количество                        10                  7               5
# цена                              5999                2499            3999
# вес                               5                   2               3
# тип/цветопередача/формат          jet                 color           A4

# Конечно, можно было бы еще учесть ошибку, если вводили не те типы принтеров, цветопередачи и тд,
#                                           но я оставила возможность ввода пустой строки, если это заранее неизвестно
