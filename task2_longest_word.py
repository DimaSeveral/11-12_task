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

if __name__ == "__main__":
    print(find_longest_words('Hooooorse chair post'))
#input 'Hooooorse chair post'
#output (['Hooooorse'],9)