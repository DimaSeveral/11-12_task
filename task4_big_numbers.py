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

if __name__ == "__main__":
    print(process_big_numbers([555],[555],'add'))
#input [555], [555], 'add
#output [1,1,1,0]