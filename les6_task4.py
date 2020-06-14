# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.



class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина едет')

    def stop(self):
        print('Машина стоит')

    def turn(self, direction):
        print(f'Машина повернула {direction}')

    def show_speed(self):
        print(f"Скорость машины {self.speed}")

class TownCar(Car):
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False
    def show_speed(self):
        if int(self.speed) > 60:
            print(f'Скорость машины {self.speed} превышена!')
        else:
            print(f"Скорость машины {self.speed}")

class SportCar(Car):
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

class WorkCar(Car):
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False
    def show_speed(self):
        if int(self.speed) > 40:
            print(f'Скорость машины {self.speed} превышена!')
        else:
            print(f"скорость машины {self.speed}")

class PoliceCar(Car):
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = True

car_1 = Car(90, 'голубая', 'Toyota', False)
print(f"Машина цвета {car_1.color} модели {car_1.name}, едет со скоростью {car_1.speed} км/ч является полицейской ({car_1.is_police})")
car_1.go()
car_1.turn('влево')
car_1.show_speed()
car_1.stop()
print()

car_2 = TownCar(50, 'красная', 'Kia Rio')
print(f"Машина цвета {car_2.color} модели {car_2.name}, едет со скоростью {car_2.speed} км/ч является полицейской ({car_2.is_police})")
car_2.go()
car_2.turn('вправо')
car_2.show_speed()
car_2.stop()
print()

car_3 = SportCar(100, 'черная', 'Lamborgini')
print(f"Машина цвета {car_3.color} модели {car_3.name}, едет со скоростью {car_3.speed} км/ч является полицейской ({car_3.is_police})")
car_3.go()
car_3.turn('вправо')
car_3.show_speed()
car_3.stop()
print()

car_4 = WorkCar(70, 'белая', 'Audi')
print(f"Машина цвета {car_4.color} модели {car_4.name}, едет со скоростью {car_4.speed} км/ч является полицейской ({car_4.is_police})")
car_4.go()
car_4.turn('влево')
car_4.show_speed()
car_4.stop()
print()

car_5 = PoliceCar(80, 'бело-синяя', 'Volkswagen')
print(f"Машина цвета {car_5.color} модели {car_5.name}, едет со скоростью {car_5.speed} км/ч является полицейской ({car_5.is_police})")
car_5.go()
car_5.turn('влево')
car_5.show_speed()
car_5.stop()
print()
