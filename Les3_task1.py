# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def division(a, b):
     if b != 0 : return (a/b)
     else: return ('При делении на ноль получается расходимость, и в математике она равна ထ, но в школе на 0 делить нельзя!!!')

print('Введите делимое:')
a = float(input())
print('Введите делитель:')
b = float(input())
print('Результат деления:', division(a, b))