# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname,
#                                                                                position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
#                                                             оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
#                                                                          и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
#                                                           проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = dict_person["wage"] + dict_person["bonus"]


class Position(Worker):
    def get_full_name(self):
        print(self.name + ' ' + self.surname)

    def get_total_income(self):
        print(self._income)


dict_person = {"wage": 22000, "bonus": 5000}
person = Position("Олег", "Васьков", "менеджер")

print(person.name, ' ', person.surname, ' ', person.position)

person.get_full_name()
person.get_total_income()