

# Лабораторна робота № 4, варіант 42
# Завдання 1. Передавання зі стека до черги


def get_score(record_type, x):
    # Обчислюю оцінку запису залежно від його типу.
    if record_type == "A":
        return 4 * x

    return 2 * x + 7


def print_list(label, values):
    # Виводжу список або дефіс, якщо він порожній.
    if values:
        print(f"{label}: {' '.join(map(str, values))}")
    else:
        print(f"{label}: -")


def main():
    # Зчитую кількість команд.
    n = int(input())

    # Стек зберігає записи за принципом останній прийшов — перший вийшов.
    # Черга зберігає записи за принципом перший прийшов — перший вийшов.
    stack = []
    queue = []

    # Журнали накопичують номери записів за весь час виконання.
    transferred = []
    removed = []

    # Лічильники невдалих спроб.
    empty_s = 0
    empty_q = 0
    blocked = 0

    # Кожен новий запис отримує окремий послідовний номер.
    next_id = 1

    # Виконую команди в порядку їх надходження.
    for _ in range(n):
        command = input().split()
        action = command[0]

        if action == "ADD":
            record_type = command[1]
            x = int(command[2])

            # Зберігаю номер запису та його оцінку окремо.
            record = (next_id, get_score(record_type, x))
            stack.append(record)

            # Збільшую номер для наступного запису.
            next_id += 1

        elif action == "MOVE":
            k = int(command[1])

            # Виконую рівно k спроб перенесення.
            for _ in range(k):
                # Спочатку перевіряю, чи є записи у стеку.
                if not stack:
                    empty_s += 1

                # Якщо черга заповнена, запис залишається у стеку.
                elif len(queue) >= 4:
                    blocked += 1

                else:
                    # Переношу верхній запис стека в кінець черги.
                    record = stack.pop()
                    queue.append(record)
                    transferred.append(record[0])

        elif action == "TAKE":
            k = int(command[1])

            # Виконую рівно k спроб вилучення з черги.
            for _ in range(k):
                if queue:
                    # Вилучаю перший запис черги.
                    record = queue.pop(0)
                    removed.append(record[0])
                else:
                    empty_q += 1

    # Виводжу номери записів, що залишилися у структурах.
    print_list("S", [record[0] for record in stack])
    print_list("Q", [record[0] for record in queue])

    # Обчислюю суми оцінок записів, які ще залишилися у структурах.
    print(f"Сума S: {sum(record[1] for record in stack)}")
    print(f"Сума Q: {sum(record[1] for record in queue)}")

    # Виводжу журнали виконаних операцій.
    print_list("Перенесено", transferred)
    print_list("Вилучено", removed)

    # Виводжу підсумкові лічильники.
    print(f"Порожньо S: {empty_s}")
    print(f"Порожньо Q: {empty_q}")
    print(f"Заблоковано: {blocked}")


if __name__ == "__main__":
    main()
