# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

import random
file = open('less5_task5.txt', "w+")

# в задаче не указано сколько и какие числа вводить, поэтому я осуществила рандомную запись чисел, количество которых сами выбираем
a = int(input('Введите минимально возможное записываемое число: '))
b = int(input('Введите максимально возможное записываемое число: '))
n = int(input('Введите количство цифр, записываемых в файл: '))
for i in range(n):
    if i == n-1: file.write(str(random.randint(a, b)))
    else: file.write(str(random.randint(a, b)) + ' ')

file.seek(0)

content = file.read()
list = content.split()
summ = 0
for i in range(len(list)):
    summ = summ + int(list[i])
print('Сумма чисел в файле: ', summ)

file.close()