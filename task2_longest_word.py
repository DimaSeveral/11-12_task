import re

def find_longest_words(text: str) -> tuple[list[str], int]:
    """
    Возвращает кортеж: (список самых длинных слов, их длина).
    Регистр сохраняется как в оригинале. Знаки препинания игнорируются.
    """
    if not text.strip():
        return [], 0
    words = re.findall(r'\b\w+\b', text)
    if not words:
        return [], 0
    max_len = max(len(word) for word in words)
    longest = [word for word in words if len(word) == max_len]
    # Удаляем дубликаты, сохраняя порядок
    seen = set()
    unique_longest = []
    for w in longest:
        if w not in seen:
            unique_longest.append(w)
            seen.add(w)
    return unique_longest, max_len

def run_task2():
    """Интерфейс для задания 2: ввод текста и вывод самого длинного слова."""
    print("\n=== Задание 2: Самое длинное слово ===")
    text = input("Введите текст: ").strip()
    if not text:
        print("Текст пуст. Нечего обрабатывать.")
        return
    longest_words, length = find_longest_words(text)
    if longest_words:
        print(f"Самое длинное слово(а): {longest_words}")
        print(f"Длина: {length}")
    else:
        print("Не найдено ни одного слова.")