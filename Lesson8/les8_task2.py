# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна
#                                                        корректно обработать эту ситуацию и не завершиться с ошибкой.

class ZeroError(Exception):
    def __init__(self, text):
        self.text = text

dividend = input('Введите делимое: ')
divider = input('Введите делитель: ')
try:
    if int(divider) == 0:
        raise ZeroError('На ноль делить нельзя!')
    result = (int(dividend)/int(divider))
except ZeroError as zero:
    print(zero)
except ValueError:
    print("Введите числа!")
else:
    print(f'Результат деления: {result}')
