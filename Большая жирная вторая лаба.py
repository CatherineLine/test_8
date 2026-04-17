# coding=utf-8
import math

def my_factorial(num):
    #Вычисление факториала
    if not isinstance(num, int):
        raise TypeError("Факториал определён только для целых чисел")
    if num < 0:
        raise ValueError("Факториал не определён для отрицательных чисел")
    a = 1
    for i in range(1, num + 1):
        a = a * i
    return a

def my_sin(x):
    #Синус через ряд Тейлора: sin(x) = sum((-1)^n * x^(2n+1) / (2n+1)!)
    if not isinstance(x, (int, float)):
        raise TypeError("Аргумент должен быть числом")
    # Бесконечность не является допустимым значением
    if math.isinf(x) or math.isnan(x):
        raise ValueError("Аргумент не должен быть бесконечностью или NaN")
    result = 0
    for i in range(50):
        term = ((-1) ** i) * (x ** (2 * i + 1)) / my_factorial(2 * i + 1)
        result += term
    return result

def my_cos(x):
    #Косинус через ряд Тейлора: cos(x) = sum((-1)^n * x^(2n) / (2n)!)
    if not isinstance(x, (int, float)):
        raise TypeError("Аргумент должен быть числом")
    if math.isinf(x) or math.isnan(x):
        raise ValueError("Аргумент не должен быть бесконечностью или NaN")
    result = 0
    for i in range(50):
        term = ((-1) ** i) * (x ** (2 * i)) / my_factorial(2 * i)
        result += term
    return result

def my_ln(x):
    #Натуральный логарифм через ряд Тейлора: ln(x) = 2 * sum(((x-1)/(x+1))^(2k-1)/(2k-1))
    if not isinstance(x, (int, float)):
        raise TypeError("Аргумент должен быть числом")
    if x <= 0:
        raise ValueError("Логарифм определён только для x > 0")
    return 2 * sum(((x - 1) / (x + 1)) ** (2 * i - 1) / (2 * i - 1) for i in range(1, 100))

def my_sqrt(x):
    #Квадратный корень через метод Ньютона
    if not isinstance(x, (int, float)):
        raise TypeError("Аргумент должен быть числом")
    if x < 0:
        raise ValueError("Корень из отрицательного числа")
    if x == 0:
        return 0
    guess = x / 2
    for _ in range(50):
        guess = (guess + x / guess) / 2
    return guess

#Большая функция, 1 вариант

def func(x):
    if not isinstance(x, (int, float)):
        raise TypeError("Аргумент должен быть числом")

    if x <= 0:
        if x == 0:
            raise ValueError("ln(|0|) не определён")
        sin_val = my_sin(x)
        if sin_val < 0:
            raise ValueError("sin(x) отрицателен, корень не извлекается")
        sqrt_sin = my_sqrt(sin_val)
        ln_abs = my_ln(abs(x))
        cos_ln = my_cos(ln_abs)
        return sqrt_sin * cos_ln
    else:
        sin_val = my_sin(x)
        # Проверяем на близость к нулю (из-за погрешности ряда)
        if abs(sin_val) < 1e-10:
            raise ZeroDivisionError("sin(x) = 0, деление на ноль")
        return (1 - my_cos(x)) / sin_val

#Интеграционное тестирование

import unittest

class IntegrationTestBottomUp(unittest.TestCase):

    def test_sin_valid_boundary(self):
        #Верное граничное значение
        self.assertAlmostEqual(my_sin(0), 0, places=5)

    def test_sin_invalid_boundary(self):
        #Неверное граничное значение
        with self.assertRaises(ValueError):
            my_sin(float('inf'))

    def test_sin_valid_equivalent(self):
        #Верное эквивалентное значение
        self.assertAlmostEqual(my_sin(math.pi / 2), 1, places=3)

    def test_sin_invalid_equivalent(self):
        #Неверное эквивалентное значение
        with self.assertRaises(TypeError):
            my_sin("не число")

    def test_cos_valid_boundary(self):
        #Верное граничное значение
        self.assertAlmostEqual(my_cos(0), 1, places=5)

    def test_cos_invalid_boundary(self):
        #Неверное граничное значение
        with self.assertRaises(ValueError):
            my_cos(float('inf'))

    def test_cos_valid_equivalent(self):
        #Верное эквивалентное значение
        self.assertAlmostEqual(my_cos(math.pi), -1, places=3)

    def test_cos_invalid_equivalent(self):
        #Неверное эквивалентное значение
        with self.assertRaises(TypeError):
            my_cos([1, 2, 3])

    def test_ln_valid_boundary(self):
        #Верное граничное значение
        self.assertAlmostEqual(my_ln(1), 0, places=5)

    def test_ln_invalid_boundary(self):
        #Неверное граничное значение
        with self.assertRaises(ValueError):
            my_ln(0)

    def test_ln_valid_equivalent(self):
        #Верное эквивалентное значение
        self.assertAlmostEqual(my_ln(math.e), 1, places=2)

    def test_ln_invalid_equivalent(self):
        #Неверное эквивалентное значение
        with self.assertRaises(ValueError):
            my_ln(-5)

    def test_sqrt_valid_boundary(self):
        #Верное граничное значение
        self.assertAlmostEqual(my_sqrt(0), 0, places=5)

    def test_sqrt_invalid_boundary(self):
        #Неверное граничное значение
        with self.assertRaises(ValueError):
            my_sqrt(-0.0001)

    def test_sqrt_valid_equivalent(self):
        #Верное эквивалентное значение
        self.assertAlmostEqual(my_sqrt(4), 2, places=5)

    def test_sqrt_invalid_equivalent(self):
        #Неверное эквивалентное значение
        with self.assertRaises(ValueError):
            my_sqrt(-1)

    def test_sqrt_sin_valid_boundary(self):
        #Верное граничное значение
        self.assertAlmostEqual(my_sqrt(my_sin(0)), 0, places=5)

    def test_sqrt_sin_invalid_boundary(self):
        #Неверное граничное значение
        with self.assertRaises(ValueError):
            my_sqrt(my_sin(-0.001))

    def test_sqrt_sin_valid_equivalent(self):
        #Верное эквивалентное значение
        self.assertAlmostEqual(my_sqrt(my_sin(math.pi / 2)), 1, places=5)

    def test_sqrt_sin_invalid_equivalent(self):
        #Неверное эквивалентное значение
        with self.assertRaises(ValueError):
            my_sqrt(my_sin(-math.pi / 2))

    def test_cos_ln_abs_valid_boundary(self):
        #Верное граничное значение
        self.assertAlmostEqual(my_cos(my_ln(abs(-1))), 1, places=3)

    def test_cos_ln_abs_invalid_boundary(self):
        #Неверное граничное значение
        with self.assertRaises(ValueError):
            my_cos(my_ln(abs(0)))

    def test_cos_ln_abs_valid_equivalent(self):
        #Верное эквивалентное значение
        self.assertAlmostEqual(my_cos(my_ln(abs(-math.e))), math.cos(1), places=3)

    def test_cos_ln_abs_invalid_equivalent(self):
        #Неверное эквивалентное значение
        with self.assertRaises(TypeError):
            my_cos(my_ln(abs("строка")))

    def test_one_minus_cos_over_sin_valid_boundary(self):
        #Верное граничное значение
        small = 1e-5
        result = (1 - my_cos(small)) / my_sin(small)
        self.assertAlmostEqual(result, 0, places=3)

    def test_one_minus_cos_over_sin_invalid_boundary(self):
        #Неверное граничное значение - деление на ноль при x = π
        # Вызываем func, которая сама выбросит ZeroDivisionError
        with self.assertRaises(ZeroDivisionError):
            func(math.pi)

    def test_one_minus_cos_over_sin_valid_equivalent(self):
        #Верное эквивалентное значение
        self.assertAlmostEqual((1 - my_cos(math.pi / 2)) / my_sin(math.pi / 2), 1, places=3)

    def test_one_minus_cos_over_sin_invalid_equivalent(self):
        #Неверное эквивалентное значение - деление на ноль при x = 0 (но x = 0 даёт ValueError)
        #Для ZeroDivisionError нужен x > 0, где sin(x) = 0, например x = π
        with self.assertRaises(ZeroDivisionError):
            func(math.pi)

    def test_func_valid_boundary(self):
        #Верное граничное значение
        small = 1e-5
        self.assertAlmostEqual(func(small), 0, places=3)

    def test_func_invalid_boundary(self):
        #Неверное граничное значение
        with self.assertRaises(ValueError):
            func(0)

    def test_func_valid_equivalent(self):
        #Верное эквивалентное значение
        self.assertAlmostEqual(func(math.pi / 2), 1, places=2)

    def test_func_invalid_equivalent(self):
        #Неверное эквивалентное значение - деление на ноль при x = π
        with self.assertRaises(ZeroDivisionError):
            func(math.pi)

if __name__ == "__main__":
    unittest.main(argv=[''], verbosity=2, exit=False)