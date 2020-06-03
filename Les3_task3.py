#3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    if a>b:
        if b>c: return(a+b)
        else: return(a+c)
    else:
        if c<a: return (b+a)
        else: return (b+c)
print('Введите числа:')
a = float(input())
b = float(input())
c = float(input())

print(my_func(a,b,c))