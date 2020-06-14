# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). 
# В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки.")

class Pen(Stationery):
    def __init__(self):
        self.title = 'Pen'
    def draw(self):
        print('Запуск отрисовки ручкой')

class Pencil(Stationery):
    def __init__(self):
        self.title = 'Pencil'
    def draw(self):
        print('Запуск отрисовки карандашом')

class Handle(Stationery):
    def __init__(self):
        self.title = 'Handle'
    def draw(self):
        print('Запуск отрисовки маркером')


pencil = Pencil()
print(pencil.title)
pencil.draw()
pen = Pen()
print(pen.title)
pen.draw()
handle = Handle()
print(handle.title)
handle.draw()

pen_1 = Stationery('Pen')
print(pen_1.title)
pen_1.draw()

