def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for i in numbers:
        try:
            if isinstance(i, (int, float)):
                result += i
            else:
                raise TypeError(f"Некорректный тип данных для подсчёта суммы - {i}")
        except TypeError as e:
            print(e)
            incorrect_data += 1
    return result, incorrect_data


def calculate_average(numbers):
    try:
        if not isinstance(numbers, (list, tuple)):
            raise TypeError("В numbers записан некорректный тип данных")
        total_sum, incorrect_data = personal_sum(numbers)
        if incorrect_data > 0:
            return None


        if len(numbers) == 0:
            return 0


        return total_sum / len(numbers)

    except TypeError as e:
        print(e)
        return None
    except ZeroDivisionError:
        return 0


# Тестирование функций
print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
