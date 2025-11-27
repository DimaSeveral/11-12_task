from tasks import task1_unique_words, task2_longest_word, task4_big_numbers


def main_menu():
    while True:
        print("\n" + "="*50)
        print("Главное меню")
        print("1. Задание 1: Уникальные слова")
        print("2. Задание 2: Самое длинное слово")
        print("3. Задание 4: Большие числа")
        print("4. Выход")
        choice = input("Выберите задание (1-4): ").strip()
        
        if choice == '1':
            task1_unique_words.run_task1()
        elif choice == '2':
            task2_longest_word.run_task2()
        elif choice == '3':
            task4_big_numbers.run_task4()
        elif choice == '4':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    main_menu()