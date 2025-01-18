# Импортируем необходимые модули
from colorama import Fore, Style, init
from create_note_function import create_note
from update_note_function import update_note
from display_notes_function import display_notes, display_note
from search_notes_function import search_notes

# Инициализация colorama для автоматического сброса стилей
init(autoreset=True)


# Функция выбора номера заметки
def choice_note(notes):
    while True:
        user_input = input("Введите номер заметки (пустой ввод для \
выхода): ").strip()
        if not user_input:  # Проверка на пустой ввод
            print("Выход из выбора заметки.")
            return None
        try:
            note_index = int(user_input) - 1  # Преобразование ввода в индекс
            if 0 <= note_index < len(notes):  # Проверка корректности индекса
                return note_index
            print("Такой заметки не существует")  # Сообщение об ошибке
        except ValueError:
            print("Введите число.")  # Обработка некорректного ввода


# Функция для удаления заметки
def delete_note(notes):
    display_notes(notes)  # Отображение всех заметок
    while True:
        user_input = input(Fore.YELLOW + "Введите номер заметки для \
удаления (пустой ввод для выхода): " + Style.RESET_ALL).strip()
        if not user_input:  # Проверка на пустой ввод
            print(Fore.YELLOW + "Выход из удаления заметки." + Style.RESET_ALL)
            return
        try:
            note_index = int(user_input) - 1  # Преобразование ввода в индекс
            if 0 <= note_index < len(notes):  # Проверка корректности индекса
                confirm = input(Fore.RED + "Вы уверены, что хотите удалить \
эту заметку? (да/нет): " + Style.RESET_ALL).lower()
                if confirm == 'да':  # Подтверждение удаления
                    del notes[note_index]  # Удаление заметки
                    print(Fore.GREEN + "Заметка удалена!" + Style.RESET_ALL)
                    return
                print(Fore.YELLOW + "Удаление отменено." + Style.RESET_ALL)
                return
            print(Fore.RED + "Неверный номер \
заметки." + Style.RESET_ALL)  # Сообщение об ошибке
        except ValueError:
            print(Fore.RED + "Ошибка: введите число или оставьте поле пустым \
для выхода." + Style.RESET_ALL)  # Обработка некорректного ввода


# Основные функции для меню
def create_new_note():
    new_note = create_note()  # Создание новой заметки
    notes.append(new_note)  # Добавление заметки в список
    print(Fore.GREEN + "Заметка создана:" + Style.RESET_ALL)
    display_note(new_note, len(notes))  # Отображение созданной заметки


def update_existing_note():
    display_notes(notes)  # Отображение всех заметок
    if not notes:  # Проверка на наличие заметок
        print("Нет заметок для изменения.")
        return
    note_index = choice_note(notes)  # Выбор заметки для обновления
    if note_index is not None:
        # Обновление заметки
        updated_note = update_note(notes[note_index])
        # Замена старой заметки на обновленную
        notes[note_index] = updated_note
        print(Fore.GREEN + "Заметка обновлена:" + Style.RESET_ALL)
        # Отображение обновленной заметки
        display_note(updated_note, note_index + 1)


def search_notes_menu():
    found_notes = search_notes(notes)  # Поиск заметок
    if found_notes:
        print(Fore.GREEN + "\nНайденные заметки:" + Style.RESET_ALL)
        # Отображение найденных заметок
        for i, note in enumerate(found_notes, start=1):
            display_note(note, i)
    else:
        print(Fore.RED + "Заметки, соответствующие запросу, \
не найдены." + Style.RESET_ALL)  # Сообщение о отсутствии найденных заметок


# Функция для отображения меню и обработки выбора пользователя
def menu():
    actions = {
        '1': create_new_note,  # Создание новой заметки
        '2': lambda: display_notes(notes),  # Отображение всех заметок
        '3': update_existing_note,  # Обновление заметки
        '4': lambda: delete_note(notes),  # удаление заметки
        '5': search_notes_menu,  # поиск заметок
        '6': lambda: print(Fore.GREEN + "Программа завершена. Спасибо за \
использование!" + Style.RESET_ALL) or exit()  # Выход из программы
    }

    while True:
        print(Fore.CYAN + "\nМеню действий:" + Style.RESET_ALL)
        print("1. Создать новую заметку")
        print("2. Показать все заметки")
        print("3. Обновить заметку")
        print("4. Удалить заметку")
        print("5. Найти заметки")
        print("6. Выйти из программы")

        # Получение выбора пользователя
        choice = input(Fore.YELLOW + "Ваш выбор: " + Style.RESET_ALL)
        # Получение соответствующего действия
        action = actions.get(choice, lambda: print(Fore.RED + "Неверный \
выбор. Пожалуйста, выберите действие из списка." + Style.RESET_ALL))
        action()  # Выполнение действия


# Основная функция для запуска программы
def main():
    print(Fore.CYAN + "Добро пожаловать в 'Менеджер \
заметок'!" + Style.RESET_ALL)
    menu()  # Вызов функции меню


# Точка входа
if __name__ == "__main__":

    # Список заметок
    notes = [
        {
            'username': 'Алексей',  # Имя пользователя
            'titles': ['Список покупок'],  # Заголовок заметки
            'content': 'Купить продукты на неделю',  # Содержимое заметки
            'status': 'новая',  # Статус заметки
            'created_date': '12-01-2025',  # Дата создания заметки
            'issue_date': '13-02-2025'  # Дата завершения заметки
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

    main()  # Запуск основной функции
