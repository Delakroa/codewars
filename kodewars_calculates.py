# Calculate average
# Напишите функцию, которая вычисляет среднее значение чисел в данном списке.
# Примечание: пустые массивы должны вернуть 0.
# Кусок теста который должен пройти

# def fixed_tests():
#     @test.it('Basic Test Cases')
#     def basic_test_cases():
#         test.assert_equals(find_average([1, 2, 3]), 2)

# --------------------------------------------------------------------------------------

# from statistics import mean


# На codewars данный вариант не работает
# def find_average(*args: int):
#     """Среднее вычисление массива"""
#     try:
#         average_a = mean([*args])
#
#         return average_a
#
#     except statistics.StatisticsError:
#         return 0
#
#
# print(find_average(123, 43, 32))

# --------------------------------------------------------------------------------------

def find_average(numbers):
    """Второй вариант расчета среднего значения.
    Данный код прошел все тесты на codewars"""
    try:
        return sum(numbers) / len(numbers)
    except ZeroDivisionError:
        return 0


# --------------------------------------------------------------------------------------

