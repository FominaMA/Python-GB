#5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.

rating = ['7', '5', '3', '3', '2']
new_element = str(input("Введите новый элемент рейтинга:"))

for i in range(1, len(rating), 1):
    if new_element == rating[i]:
        rating.insert(i+1, new_element)
        break
    elif new_element > rating[i]:
        rating.insert(i-1, new_element)
        break
    elif i + 1 == len(rating) and new_element < rating[i]:
        rating.append(new_element)
        break
print(rating)