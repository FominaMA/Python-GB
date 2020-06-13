# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

file = open('less5_task1.txt', "w")
i = 1
list = []
while True:
    line = input(f"Введите строку {i}: ")
    i += 1
    if line == '':
         break
    else:
         dop_line = line + '\n'
         list.append(dop_line)
         continue

file.writelines(list)
file.close()
