# Напишите функцию, которая вычисляет среднее значение чисел в данном списке.

# Примечание: пустые массивы должны вернуть 0.

# Кусок теста который должен пройти

# def fixed_tests():
#     @test.it('Basic Test Cases')
#     def basic_test_cases():
#         test.assert_equals(find_average([1, 2, 3]), 2)

from statistics import mean


def calculates_the_average():
    """Среднее вычисление массива"""
    a = (1, 2, 3, 4, 5)
    average_a = mean(a)
    return average_a


print(calculates_the_average())
