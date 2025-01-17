# Импортируем необходимые модули
from colorama import Fore, Style, init
from create_note_function import create_note
from update_note_function import update_note
from display_notes_function import display_notes, display_note
from search_notes_function import search_notes

# Инициализация colorama
init(autoreset=True)


# Функция выбора номера заметки
def choice_note(notes):
    check_size = len(notes)
    while True:
        try:
            user_input = input("Введите номер заметки, которую нужно \
изменить (пустой ввод для выхода): ")

            # Если ввод пустой, выходим из функции
            if user_input.strip() == "":
                print("Выход из выбора заметки.")
                return None

            my_note = int(user_input)
            if 1 <= my_note <= check_size:
                return my_note - 1  # Возвращаем индекс заметки
            else:
                print("Такой заметки не существует")
        except ValueError:
            print("Введите номер заметки - число")


# Функция для удаления заметки
def delete_note(notes):
    display_notes(notes)  # Показываем все заметки
    while True:
        user_input = input(
            Fore.YELLOW + "Введите номер заметки для удаления (пустой ввод \
для выхода): " + Style.RESET_ALL)

        # Если ввод пустой, выходим из функции
        if user_input.strip() == "":
            print(Fore.YELLOW + "Выход из удаления заметки." + Style.RESET_ALL)
            return

        try:
            # Преобразуем ввод в индекс
            note_index = int(user_input) - 1
            # Проверяем, что индекс в допустимых пределах
            if 0 <= note_index < len(notes):
                confirm = input(Fore.RED + "Вы уверены, что хотите удалить \
эту заметку? (да/нет): " + Style.RESET_ALL)
                if confirm.lower() == 'да':
                    del notes[note_index]
                    print(Fore.GREEN + "Заметка удалена!" + Style.RESET_ALL)
                    return  # Выходим после удаления
                else:
                    print(Fore.YELLOW + "Удаление отменено." + Style.RESET_ALL)
                    return  # Выходим после отмены
            else:
                print(Fore.RED + "Неверный номер заметки." + Style.RESET_ALL)
        except ValueError:  # Обработка неправильного ввода (не число)
            print(Fore.RED + "Ошибка: введите число или оставьте поле пустым \
для выхода." + Style.RESET_ALL)


# Функция для отображения меню и обработки выбора пользователя
def menu():
    while True:
        print(Fore.CYAN + "\nМеню действий:" + Style.RESET_ALL)
        print("1. Создать новую заметку")
        print("2. Показать все заметки")
        print("3. Обновить заметку")
        print("4. Удалить заметку")
        print("5. Найти заметки")
        print("6. Выйти из программы")

        choice = input(Fore.YELLOW + "Ваш выбор: " + Style.RESET_ALL)

        if choice == '1':
            # Вызов функции для создания заметки и добавление заметки в список
            new_note = create_note()  # Создаем новую заметку
            notes.append(new_note)  # Добавляем её в список
            print(Fore.GREEN + "Заметка создана:" + Style.RESET_ALL)
            display_note(new_note, len(notes))  # Выводим новую заметку
        elif choice == '2':
            display_notes(notes)  # Вывод всех заметок
        elif choice == '3':
            display_notes(notes)  # Вывод всех заметок
            if len(notes):
                # Получаем индекс заметки для обновления
                note_index = choice_note(notes)
                # Проверяем, не был ли ввод пустым
                if note_index is not None:
                    # Обновляем заметку
                    updated_note = update_note(notes[note_index])
                    # Сохраняем обновленную заметку в списке
                    notes[note_index] = updated_note
                    print(Fore.GREEN + "Заметка обновлена:" + Style.RESET_ALL)
                    # Выводим обновленную заметку
                    display_note(updated_note, note_index + 1)
            else:
                print("Нет заметок для изменения")
        elif choice == '4':
            delete_note(notes)  # Передаем notes в функцию delete_note
        elif choice == '5':
            # Вызов функции поиска заметок
            found_notes = search_notes(notes)
            if found_notes:
                print(Fore.GREEN + "\nНайденные заметки:" + Style.RESET_ALL)
                for i, note in enumerate(found_notes, start=1):
                    display_note(note, i)
            else:
                print(Fore.RED + "Заметки, соответствующие запросу, \
не найдены." + Style.RESET_ALL)
        elif choice == '6':
            print(Fore.GREEN + "Программа завершена. Спасибо за \
использование!" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Неверный выбор. Пожалуйста, выберите действие \
из списка." + Style.RESET_ALL)


# Основная функция для запуска программы
def main():
    print(
        Fore.CYAN + "Добро пожаловать в 'Менеджер заметок'!" +
        Style.RESET_ALL
    )
    menu()


# точка входа
if __name__ == "__main__":
    # Список для хранения всех заметок
    notes = [
        {
            'username': 'Алексей',
            'titles': ['Список покупок'],
            'content': 'Купить продукты на неделю',
            'status': 'новая',
            'created_date': '12-01-2025',
            'issue_date': '13-02-2025'
        },
        {
            'username': 'Мария',
            'titles': ['Учеба', 'Спорт'],
            'content': 'Подготовиться к экзамену',
            'status': 'в процессе',
            'created_date': '01-01-2025',
            'issue_date': '25-06-2025'
        }
    ]

    # Запуск основной функции
    main()
