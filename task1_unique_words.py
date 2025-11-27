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

if __name__ == "__main__":
    print(find_unique_words('abc abc cab bac'))
#input (abc abc cab bac)
#output ['cab', 'bac']    
