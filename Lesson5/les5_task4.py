# 4. Создать (не программно) текстовый файл со следующим содержимым:
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

file_1 = open('less5_task4_1.txt', "r")
file_2 = open('less5_task4_2.txt', "w")
list_file_2 = []

for line in file_1:
    list = line.split()
    if list[0] == 'One': list[0] = 'Один'
    elif list[0] == 'Two': list[0] = 'Два'
    elif list[0] == 'Three': list[0] = 'Три'
    elif list[0] == 'Four': list[0] = 'Четыре'
    list_file_2.append(list[0] + ' ' + list[1] + ' ' + list[2] + '\n')

file_2.writelines(list_file_2)
file_1.close()
file_2.close()
