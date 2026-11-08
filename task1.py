
# Лабораторна робота № 4, варіант 42
# Завдання 1. Перша позиція точного збігу за цілою часткою


def linear_search(numbers, t):
    # Послідовно перевіряю всі числа у початковому списку.
    positions = []

    for i in range(len(numbers)):
        if numbers[i] // 4 == t:
            positions.append(i)

    # Повертаю найменшу початкову позицію.
    if positions:
        return min(positions)

    return None


def binary_search(sorted_numbers, t):
    # Знаходжу ліву межу блоку чисел із потрібним ключем.
    left = 0
    right = len(sorted_numbers)

    while left < right:
        middle = (left + right) // 2

        if sorted_numbers[middle][0] < t:
            left = middle + 1
        else:
            right = middle

    first = left

    # Якщо потрібного ключа немає, повертаю None.
    if first == len(sorted_numbers) or sorted_numbers[first][0] != t:
        return None

    # Знаходжу праву межу блоку однакових ключів.
    left = first
    right = len(sorted_numbers)

    while left < right:
        middle = (left + right) // 2

        if sorted_numbers[middle][0] <= t:
            left = middle + 1
        else:
            right = middle

    last = left

    # Серед усього знайденого блоку шукаю
    # найменшу початкову позицію.
    positions = []

    for i in range(first, last):
        positions.append(sorted_numbers[i][1])

    return min(positions)


def main():
    # Зчитую всі вхідні дані.
    import sys
    data = list(map(int, sys.stdin.read().split()))

    n = data[0]

    # Зберігаю початкові числа.
    numbers = data[1:n + 1]

    # Створюю список ключів та початкових позицій.
    sorted_numbers = []

    for i in range(n):
        sorted_numbers.append((numbers[i] // 4, i))

    # Упорядковую числа за їхніми ключами.
    sorted_numbers.sort(key=lambda item: item[0])

    # Зчитую кількість запитів.
    q = data[n + 1]

    # Виконую кожен запит.
    for i in range(q):
        t = data[n + 2 + i]

        linear_result = linear_search(numbers, t)
        binary_result = binary_search(sorted_numbers, t)

        # Виводжу результат лінійного пошуку.
        if linear_result is None:
            print("Лінійний: немає")
        else:
            print(f"Лінійний: {linear_result}")

        # Виводжу результат бінарного пошуку.
        if binary_result is None:
            print("Бінарний: немає")
        else:
            print(f"Бінарний: {binary_result}")


if __name__ == "__main__":
    main()
