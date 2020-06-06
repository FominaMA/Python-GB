#6. * Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

products_list = []
n = int(input("Введите количество товаров: ")) # n - количество товаров в структуре
dict_product = dict()
name_list = []
price_list = []
amount_list = []
measure_list = []
# Заполняем данные по товарам (чтобы много не писать я забивала 3 товара)
for i in range(n):
    name = input(f"Введите название товара {i+1}: ")
    price = input(f"Введите цену товра {i+1}: ")
    amount = input(f"Введите количество товара {i+1}: ")
    measure = input(f"Введите ед измерения товара {i+1}: ")
    dict_product = {"название": name, "цена": price, "кол-во": amount, "ед": measure}
    cort = (i+1, dict_product)
    products_list.append(cort)
print(products_list)

for i in range(len(products_list)):
    cort = products_list[i]
    name_list.append(cort[1].get("название"))
    price_list.append(cort[1].get("цена"))
    amount_list.append(cort[1].get("кол-во"))
    measure_list.append(cort[1].get("ед"))
dict_product = {"название": name_list, "цена": price_list, "кол-во": amount_list, "ед": measure_list}
print(dict_product)

    # products_list[i] = (number, discription)
    # number = i + 1






# a = 'hello'
# b = 1
# k = (a, b)
# print(k)