# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату
#                                                                               в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Data:
    @classmethod
    def number(cls, data):
        list = data.split('.')
        number = [int(el) for el in list]
        print(number[0],' ', number[1], ' ', number[2], type(number[1]))

    @staticmethod
    def validate(data):
        list = data.split('.')
        list_int  = [int(el) for el in list]
        if list_int[1] > 12 or list_int[1] < 1:
            print ('В году 12 месяцев!')
        else:
            if list_int[0] > 31 or list_int[0] < 1:
                print('В месяце 31 день!')
            elif list_int[0] == 31 and list_int[1] < 8 and (list_int[1] % 2) == 0 and list_int[1] != 2:
                print(f'В {list_int[1]}ом месяце только 30 дней!')
            elif list_int[0] == 31 and list_int[1] > 7 and (list_int[1] % 2) == 1 and list_int[1] != 2:
                print(f'В {list_int[1]}ом этом месяце только 30 дней!')
            elif list_int[1] == 2 and list_int[0] > 28:
                print(f'В {list_int[1]}ом месяце только 28 дней!')
            else: print('Проверка прошла успешно!')



Data.number('12.12.1997')
# проверяем дни:
Data.validate('31.05.1997')
Data.validate('31.04.1997')
Data.validate('30.02.1997')
Data.validate('37.12.1997')
Data.validate('-5.12.1997')
# проверяем месяц
Data.validate('31.15.1997')
Data.validate('31.-5.1997')
Data.validate('14.02.1997')

