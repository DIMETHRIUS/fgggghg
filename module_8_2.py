
def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for i in range(numbers):
        result += 1
        try:
            if not isinstance(numbers, (int, float)):
                incorrect_data += 1
        except TypeError:
            return incorrect_data
    return result, incorrect_data


def calculate_average(numbers):
    try:
        if not isinstance(numbers, (list, tuple)):
            raise TypeError("В numbers записан некорректный тип данных")

        total = personal_sum(numbers)
        average = total / len(numbers)
        return average

    except ZeroDivisionError:
        return 0

    except TypeError as exc:
        print(exc)
        return None
print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать



