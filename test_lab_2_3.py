import unittest
import math

def my_sort(unsorted): # сортировка
    if not (all(isinstance(item, (int, float)) for item in unsorted)
            and isinstance(unsorted, list)):
        raise ValueError('Аргументом функции должен являться список чисел (int или float)')

    a = 0
    for i in range(0, len(unsorted)):
        for j in range(0, len(unsorted)-1):
            if unsorted[j] > unsorted[j+1]:
                a = unsorted[j+1]
                unsorted[j+1] = unsorted[j]
                unsorted[j] = a
    return unsorted


def get_fib(n): # вычисление числа Фибоначчи
    if n < 0 or not isinstance(n, int):
        raise ValueError('Аргументом должно быть натуральное число')

    a = []
    a.append(1)
    a.append(1)
    if n > 2:
        for i in range(2,n):
            a.append(a[i-1]+a[i-2])
    return a[n-1]

def is_pal(st): # проверка на палиндром
    if not isinstance(st, str):
        raise TypeError('Аргументом функции должна быть строка')

    result = True
    for i in range(0, len(st)):
        if st[i] != st[len(st)-i-1]:
            result = False
    return result


def my_factorial(num): # вычисление факториала
    if num < 0 or not (isinstance(num, int)):
        raise ValueError('Аргементом функции должно являться целое число больше нуля')

    a = 1
    if num > 1:
        for i in range(1, num+1):
            a = a * i
    return a


def my_pow(num, st): # возведение в степень
    if num < 0 or not isinstance(st, (int, float)) or not isinstance(num, (int, float)):
        raise ValueError('Аргументы должны быть действительными числами')

    return num**st


def my_is_simple(num): # проверка числа на простоту
    if not isinstance(num, int) or num < 0:
        raise ValueError('Аргументом функции должно являться натуральное число')

    res = True
    if num > 0:
        for i in range(2, math.ceil(num/2) + 1):
            if num % i == 0 and num != 2:
                res = False
    return res

def my_sin(x):
    result = 0
    for i in range(50):
        term = ((-1) ** i) * (x ** (2 * i + 1)) / my_factorial(2 * i + 1)
        result += term
    return result


def my_cos(x):
    c = 2
    n = 0
    for i in range(50):
        if i % 2 == 0:
            n += ((x ** c) / my_factorial(c))
        else:
            n -= ((x ** c) / my_factorial(c))
        c += 2
    return 1 - n


def my_ln(x):
    return 2*sum(((x-1)/(x+1))**i/i for i in range(1, 100, 2))


def func(x):
    if x < 0:
        result = my_sin(x)**2 + my_cos(x)**2 + my_ln(my_sin(x))
    else:
        result = (my_sin(x**2) + my_cos(my_ln(x**2)))**0.5
    return result


def my_subfunc_1(x):
    return my_cos(my_ln(x ** 2))


def my_subfunc_2(x):
    return my_ln(my_sin(x))


class TestFunctions(unittest.TestCase):
    def test_sort(self):
        # случай 1
        test_list_1 = [3, 2, 1.5]
        self.assertEqual(my_sort(test_list_1), [1.5, 2, 3], "Должно быть [1.5, 2, 3]")
        # случай 2
        test_list_2 = [-5, 4, -3, 2, 0]
        self.assertEqual(my_sort(test_list_2), [-5, -3, 0, 2, 4], "Должно быть [-5, -3, 0, 2, 4]")
        # случай 3: неправильный ввод
        with self.assertRaises(ValueError):
            my_sort([[0, 1], 1, 2, 5, -1])
        # случай 4: неправильный ввод
        with self.assertRaises(ValueError):
            my_sort(['-2', 1, 2, 5, -1])
        # случай 5: неправильный ввод
        with self.assertRaises(TypeError):
            my_sort(-2, 2, 5, -1)
        # случай 6: неправильный ввод
        with self.assertRaises(TypeError):
            my_sort(112)



    def test_is_pal(self):
        # случай 1
        test_string_1 = "собака"
        self.assertEqual(is_pal(test_string_1), False, "Должно получиться False")
        # случай 2
        test_string_2 = "тот"
        self.assertEqual(is_pal(test_string_2), True, "Должно получиться True")
        # случай 3
        with self.assertRaises(TypeError):
            is_pal(1221)
        # случай 4
        with self.assertRaises(TypeError):
            is_pal([0, 1, 1, 0])


    def test_factioral(self):
        #  случай 1
        test_num_1 = 0
        self.assertEqual(my_factorial(test_num_1), 1, "Должно получиться 1")
        #  случай 2
        test_num_2 = 3
        self.assertEqual(my_factorial(test_num_2), 6, "Должно получиться 6")
        #  случай 3
        test_num_3 = 5
        self.assertEqual(my_factorial(test_num_3), 120, "Должно получиться 120")
        # случай 4
        with self.assertRaises(ValueError):
            my_factorial(-5)
        # случай 5
        with self.assertRaises(TypeError):
            my_factorial([-5, 2, 3])

    def test_fib(self):
        test_num_1 = 3
        self.assertEqual(get_fib(test_num_1), 2, "Должно получиться 2")
        test_num_2 = 1
        self.assertEqual(get_fib(test_num_2), 1, "Должно получиться 1")
        test_num_3 = 5
        self.assertEqual(get_fib(test_num_3), 5, "Должно получиться 5")
        with self.assertRaises(ValueError):
            get_fib(-10)
        with self.assertRaises(TypeError):
            get_fib([-10, 5])

    def test_pow(self):
        test_nums_1 = [5, 2]
        self.assertEqual(my_pow(test_nums_1[0], test_nums_1[1]), 25, "Должно получиться 25")
        test_nums_2 = [2, 3]
        self.assertEqual(my_pow(test_nums_2[0], test_nums_2[1]), 8, "Должно получиться 8")
        test_nums_3 = [3, 4]
        self.assertEqual(my_pow(test_nums_3[0], test_nums_3[1]), 81, "Должно получиться 81")
        with self.assertRaises(ValueError):
            my_pow(-5, 2)
        with self.assertRaises(TypeError):
            my_pow([-5, 2], 2)

    def test_is_simple(self):
        test_num_1 = 5
        self.assertEqual(my_is_simple(test_num_1), True, "Должно получиться True")
        test_num_2 = 10
        self.assertEqual(my_is_simple(test_num_2), False, "Должно получиться False")
        test_num_3 = 11
        self.assertEqual(my_is_simple(test_num_3), True, "Должно получиться True")
        with self.assertRaises(ValueError):
            my_is_simple(-5)
        with self.assertRaises(ValueError):
            my_is_simple(2.3)
        with self.assertRaises(ValueError):
            my_is_simple([2, 3, 4])

    def test_sin(self):
        test_num_1 = 0
        self.assertEqual(round(my_sin(test_num_1), 3), 0, "Ожидается 0")
        test_num_2 = 3.1415/2
        self.assertEqual(round(my_sin(test_num_2), 3), 1, "Ожидается 1")
        test_num_3 = 3.1415*1.5
        self.assertEqual(round(my_sin(test_num_3), 0), -1, "Ожидается -1")

    def test_cos(self):
        test_num_1 = 0
        self.assertEqual(my_cos(test_num_1), 1, "Ожидается 1")
        test_num_2 = 3.1415/2
        self.assertEqual(round(my_cos(test_num_2), 2), 0, "Ожидается 0")
        test_num_3 = 3.1415
        self.assertEqual(round(my_cos(test_num_3)), -1, "Ожидается -1")

    def test_ln(self):
        test_num_1 = 1
        self.assertEqual(my_ln(test_num_1), 0, "Ожидается 0")
        test_num_2 = 2.71
        self.assertEqual(round(my_ln(test_num_2), 2), 1, "Ожидается 1")

    def test_subfunc_1(self):
        self.assertEqual(round(my_subfunc_1(2.71**(3.1415*0.5)), 3), -1, 'Ожидается -1')

    def test_subfunc_2(self):
        self.assertEqual(round(my_subfunc_2(3.1415/2), 3), 0, 'Ожидается 0')

    def test_func(self):
        test_num_1 = 1
        self.assertEqual(round(func(test_num_1), 1), round(1.9**0.5, 1), "Ожидается примерно sqrt(1.9)")
        test_num_2 = -3.1415*1.5
        self.assertEqual(round(func(test_num_2), 1), 1, "Ожидается 1")

if __name__ == '__main__':
    unittest.main(verbosity=2)