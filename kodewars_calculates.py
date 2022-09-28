# Напишите функцию, которая вычисляет среднее значение чисел в данном списке.
# Примечание: пустые массивы должны вернуть 0.
# Кусок теста который должен пройти

# def fixed_tests():
#     @test.it('Basic Test Cases')
#     def basic_test_cases():
#         test.assert_equals(find_average([1, 2, 3]), 2)

from statistics import mean


def calculates_the_average(*args: int):
    """Среднее вычисление массива"""
    try:
        average_a = mean([*args])

        return average_a

    except statistics.StatisticsError:
        return 0


print(calculates_the_average(123, 43, 32))


