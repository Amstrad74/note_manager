# Импортируем необходимые модули
from colorama import Fore, Style, init
from create_note_function import create_note
from update_note_function import update_note
from display_notes_function import display_notes, display_note
from search_notes_function import search_notes

# Инициализация colorama для автоматического сброса стилей
init(autoreset=True)

# Функция выбора номера заметки. Запрашивает у пользователя номер
# заметки и возвращает индекс выбранной заметки.
def choice_note(notes):
    while True:
        user_input = input(
            "Введите номер заметки (пустой ввод для выхода): "
        ).strip()
        if not user_input:
            print("Выход из выбора заметки.")
            return None
        try:
            note_index = int(user_input) - 1
            if 0 <= note_index < len(notes):
                return note_index
            print("Такой заметки не существует")
        except ValueError:
            print("Введите число.")

# Функция для удаления заметки. Запрашивает у пользователя номер заметки
# для удаления. Удаляет заметку, если пользователь подтверждает действие.
def delete_note(notes):
    display_notes(notes)
    note_index = choice_note(notes)
    if note_index is not None:
        confirm = input(
            Fore.RED +
            "Вы уверены, что хотите удалить эту заметку? (да/нет): " +
            Style.RESET_ALL
        ).lower()
        if confirm == 'да':
            del notes[note_index]
            print(Fore.GREEN + "Заметка удалена!" + Style.RESET_ALL)
        else:
            print(Fore.YELLOW + "Удаление отменено." + Style.RESET_ALL)

# Основные функции для меню. Создает новую заметку, добавляет её в список
# и отображает информацию о ней.
def create_new_note(notes):
    new_note = create_note()
    notes.append(new_note)
    print(Fore.GREEN + "Заметка создана:" + Style.RESET_ALL)
    display_note(new_note, len(notes))

# Запрашивает у пользователя номер заметки для обновления.
# Обновляет выбранную заметку и отображает её информацию.
def update_existing_note(notes):
    display_notes(notes)
    if not notes:
        print("Нет заметок для изменения.")
        return
    note_index = choice_note(notes)
    if note_index is not None:
        updated_note = update_note(notes[note_index])
        notes[note_index] = updated_note
        print(Fore.GREEN + "Заметка обновлена:" + Style.RESET_ALL)
        display_note(updated_note, note_index + 1)

# Запрашивает у пользователя критерии поиска и отображает найденные заметки.
# Если заметки не найдены, выводит соответствующее сообщение.
def search_notes_menu(notes):
    found_notes = search_notes(notes)
    if found_notes:
        print(Fore.GREEN + "\nНайденные заметки:" + Style.RESET_ALL)
        for i, note in enumerate(found_notes, start=1):
            display_note(note, i)
    else:
        print(
            Fore.RED + "Заметки, соответствующие запросу, не найдены." +
            Style.RESET_ALL
        )

# Функция для отображения меню и обработки выбора пользователя.
# Вызывает соответствующие функции в зависимости от выбора.
def menu(notes):
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
            create_new_note(notes)
        elif choice == '2':
            display_notes(notes)
        elif choice == '3':
            update_existing_note(notes)
        elif choice == '4':
            delete_note(notes)
        elif choice == '5':
            search_notes_menu(notes)
        elif choice == '6':
            print(
                Fore.GREEN +
                "Программа завершена. Спасибо за использование!" +
                Style.RESET_ALL
            )
            break
        else:
            print(
                Fore.RED +
                "Неверный выбор. Пожалуйста, выберите действие из списка." +
                Style.RESET_ALL
            )


# Основная функция для запуска программы
def main(notes):
    print(
        Fore.CYAN + "Добро пожаловать в 'Менеджер заметок'!" + Style.RESET_ALL
    )
    menu(notes)

# Точка входа
if __name__ == "__main__":
    # Список заметок
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

    main(notes)  # Запуск основной функции
