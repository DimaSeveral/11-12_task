def run_task4():
    """Интерфейс для задания 4: операции с большими числами."""
    print("\n=== Задание 4: Операции с большими числами ===")
    print("Числа вводятся как массивы цифр (например, [1,2,3] = 123)")
    
    try:
        a_str = input("Введите первое число (цифры через пробел): ").strip()
        if not a_str:
            print("Пустой ввод.")
            return
        a = list(map(int, a_str.split()))
        
        b_str = input("Введите второе число (цифры через пробел): ").strip()
        if not b_str:
            print("Пустой ввод.")
            return
        b = list(map(int, b_str.split()))
        
        op = input("Операция (add/sub): ").strip().lower()
        if op not in ['add', 'sub']:
            print("Неверная операция. Доступно: add, sub")
            return
        
        # Здесь можно добавить реализацию операций (как в предыдущих итерациях)
        # Для примера — просто выводим результат
        result = process_big_numbers(a, b, op)
        print(f"\nРезультат: {result}")
        
    except Exception as e:
        print(f"Ошибка при обработке: {e}")


def process_big_numbers(a: list[int], b: list[int], operation: str) -> list[int]:
    """Заглушка — вернёт сумму/разность как простой список."""
    if operation == 'add':
        # Пример: сложение как целых чисел
        num_a = int(''.join(map(str, a)))
        num_b = int(''.join(map(str, b)))
        result = num_a + num_b
        return [int(d) for d in str(result)]
    elif operation == 'sub':
        num_a = int(''.join(map(str, a)))
        num_b = int(''.join(map(str, b)))
        result = num_a - num_b
        if result < 0:
            print("Результат отрицательный — не поддерживается в текущей реализации.")
            return []
        return [int(d) for d in str(result)]
    else:
        raise ValueError("Unsupported operation")