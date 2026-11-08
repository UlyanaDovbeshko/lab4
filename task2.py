


# Лабораторна робота № 4, варіант 42
# Завдання 2. Останні елементи після сортування за значенням

import sys


def print_list(label, values):
    # Виводжу список або слово "немає", якщо він порожній.
    if values:
        print(f"{label}: {' '.join(map(str, values))}")
    else:
        print(f"{label}: немає")


def insertion_sort(data):
    # Створюю копію списку, щоб не змінювати початкові дані.
    result = data[:]

    # Починаю сортування з другого елемента.
    for i in range(1, len(result)):
        current = result[i]
        j = i - 1

        # Переміщую менші елементи вправо.
        # Однакові числа залишаю у початковому порядку.
        while j >= 0 and result[j][0] < current[0]:
            result[j + 1] = result[j]
            j -= 1

        # Вставляю елемент на його місце.
        result[j + 1] = current

    return result


def merge_sort(data):
    # Якщо залишився один або жодного елемента, повертати нічого не потрібно.
    if len(data) <= 1:
        return data[:]

    # Ділю список на дві частини.
    middle = len(data) // 2
    left = merge_sort(data[:middle])
    right = merge_sort(data[middle:])

    # Об'єдную дві відсортовані частини.
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        # Порівнюю саме значення чисел.
        # При рівності спочатку беру лівий елемент,
        # щоб зберегти початковий порядок.
        if left[i][0] >= right[j][0]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Додаю елементи, які залишилися.
    result.extend(left[i:])
    result.extend(right[j:])

    return result


def main():
    # Зчитую всі вхідні дані.
    # Також це дозволяє правильно обробити порожній список.
    data = sys.stdin.read().split()

    n = int(data[0])

    # Зберігаю кожне число разом з його початковою позицією.
    numbers = []

    for i in range(n):
        x = int(data[i + 1])
        numbers.append((x, i))

    # Зчитую кількість останніх елементів.
    k = int(data[n + 1])

    # Виконую сортування двома способами.
    insertion_result = insertion_sort(numbers)
    merge_result = merge_sort(numbers)

    # Виводжу числа після сортування вставками.
    print_list("Вставки", [item[0] for item in insertion_result])

    # Виводжу числа після сортування злиттям.
    print_list("Злиття", [item[0] for item in merge_result])

    # Виводжу початкові позиції відсортованих чисел.
    print_list("Позиції", [item[1] for item in insertion_result])

    # Вибираю останні k елементів після сортування.
    last_elements = insertion_result[-min(k, n):] if k > 0 else []

    # Виводжу останні елементи у потрібному порядку.
    print_list("Останні", [item[0] for item in last_elements])


if __name__ == "__main__":
    main()
