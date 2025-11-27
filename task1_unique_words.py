import re
from collections import Counter

def find_unique_words(text: str) -> list[str]:
    """
    Возвращает список слов, встречающихся в тексте ровно один раз.
    Регистр игнорируется. Знаки препинания не считаются частью слов.
    """
    if not text.strip():
        return []
    words = re.findall(r'\b\w+\b', text.lower())
    word_counts = Counter(words)
    return [word for word, count in word_counts.items() if count == 1]

def run_task1():
    """Интерфейс для задания 1: ввод текста и вывод уникальных слов."""
    print("\n=== Задание 1: Уникальные слова ===")
    text = input("Введите текст: ").strip()
    if not text:
        print("Текст пуст. Нечего обрабатывать.")
        return
    unique = find_unique_words(text)
    if unique:
        print("Уникальные слова:", unique)
    else:
        print("В тексте нет уникальных слов.")