# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и
#                                                                  выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class Complex_numbers:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __str__(self):
        return str(self.a) + ' + ' + str(self.b) + 'i'
    def __eq__(self, other):
        if self.a == other.a and self.b == other.b:
            return True
        else:
            return False
    def __ne__(self, other):
        if self.a == other.a and self.b == other.b:
            return False
        else:
            return True
    def __add__(self, other):
        return str(self.a + other.a) + ' + ' + str(self.b + other.b) + 'i'
    def __sub__(self, other):
        return str(self.a - other.a) + ' + ' + str(self.b - other.b) + 'i'
    def __mul__(self, other):
        return str(self.a * other.a - self.b * other.b) + ' + ' + str(self.a * other.b + self.b * other.a) + 'i'
    def __truediv__(self, other):
        k = self.a * other.a + self.b * other.b
        m = self.b * other.a - self.a * other.b
        d = other.a ** 2 + other.b ** 2
        return str(("{0:.2f}".format(k/d))) + ' + ' + str(("{0:.2f}".format(m/d))) + 'i'
    def __floordiv__(self, other):
        k = self.a * other.a + self.b * other.b
        m = self.b * other.a - self.a * other.b
        d = other.a ** 2 + other.b ** 2
        return str(int(k / d)) + ' + ' + str(int(m / d)) + 'i'
    def __pow__(self, power, modulo=None):
        # Функцию возведения комплексного числа в степень реализовала через бином Ньютона
        new_a = 0
        new_b = 0
        n = int(power)
        f_n = 1                 # n! - n факториал нужен в биноме для рассчета количичества сочетаний
        f_k = 1                 # k! - k факториал нужен в биноме для рассчета количичества сочетаний
        f_n_k = 1               # (n - k)! - (n - k) факториал нужен в биноме для рассчета количичества сочетаний
        for i in range(n + 1):
            if i == 0: f_n = 1
            else: f_n *= i
        for k in range(n + 1):
            for m in range(k + 1):
                if m == 0: f_k = 1
                else: f_k *= m
            for l in range(n - k + 1):
                if l == 0: f_n_k = 1
                else: f_n_k *= l
            koef = f_n / (f_k * f_n_k)
            if k % 4 == 0:
                new_a = new_a + koef * (self.a ** (n - k)) * (self.b ** k)
            elif k % 4 == 1:
                new_b = new_b + koef * (self.a ** (n - k)) * (self.b ** k)
            elif k % 4 == 2:
                new_a = new_a - koef * (self.a ** (n - k)) * (self.b ** k)
            elif k % 4 == 3:
                new_b = new_b - koef * (self.a ** (n - k)) * (self.b ** k)
        return str(new_a) + ' + ' + str(new_b) + 'i'

a = Complex_numbers(5, -6)
b = Complex_numbers(3, 2)
print('Число a = ', a, ', Число b = ', b)
print('Сумма равна: ', a + b)
print('Разность равна: ', a - b)
print('Произведение равно: ', a * b)
print('Деление a/b равно: ', a / b)
print('Целочисленное деление a/b равно: ', a // b)
print('a в 3 степени равно: ', a ** 3,', b в 5 степени равно: ',  b ** 5)

# Кажется, я знаю, как заполняли модуль math))))