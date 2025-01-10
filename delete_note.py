# Импортируем необходимые модули для работы с датами
from datetime import datetime

notes = []  # Список для хранения всех заметок


# Функция для проверки корректного ввода даты
def input_date(prompt):
    while True:
        try:
            date_input = input(prompt)  # Запрос ввода даты
            datetime.strptime(date_input, "%d-%m-%Y")  # Проверка формата даты
            return date_input  # Возврат корректно введенной даты
        except ValueError:
            print("Некорректный формат даты. Пожалуйста, используйте \
формат 'ДД-ММ-ГГГГ'.")


# Функция для проверки ввода "да" или "нет"
def confirm(prompt):
    while True:
        response = input(prompt).strip().lower()
        if response == 'да':
            return True
        elif response == 'нет' or response == '':
            return False
        else:
            print("Некорректный ввод. Пожалуйста, введите 'да' или 'нет'.")


# Создание нового словаря для заметки
def create_note():
    note = {}
    note["username"] = input("Введите имя пользователя: ")

    note["titles"] = []  # Инициализация списка заголовков заметки
    print("Введите заголовки заметок (оставьте пустым для завершения):")
    while True:
        title = input("Введите заголовок заметки: ")
        if title == "":
            break  # Завершение ввода, если пользователь оставил строку пустой
        if title in note["titles"]:
            print("Этот заголовок уже существует. Пожалуйста, введите \
уникальный заголовок.")
        else:
            note["titles"].append(title)  # Добавление уникального заголовка

    note["content"] = input("Введите описание заметки: ")
    note["status"] = "Не определено"  # Установка статуса заметки по умолчанию
    # Обновление статуса только если пользователь ввел статус
    if confirm("Хотите обновить статус заметки? (да/нет): "):
        update_note_status(note)  # обновление статуса заметки

    # Проверка корректного ввода даты создания заметки
    note["created_date"] = input_date("Введите дату создания заметки \
в формате 'ДД-ММ-ГГГГ': ")

    # Проверка корректного ввода даты истечения заметки
    note["issue_date"] = input_date("Введите дату истечения заметки \
в формате 'ДД-ММ-ГГГГ': ")

    notes.append(note)  # Добавление заметки в список
    print("\nЗаметка успешно добавлена!")


# Функция для отображения доступных опций статуса заметки
def display_status_options():
    print("\nВыберите текущий статус заметки:")
    print("1. Выполнено\n2. В процессе\n3. Отложено")


# Функция для обновления статуса заметки
def update_note_status(note):
    valid_statuses = {"1": "выполнено", "2": "в процессе", "3": "отложено"}
    while True:
        display_status_options()  # Вывод доступных статусов
        choice = input("Введите номер статуса либо нажмите Ввод чтобы \
оставить прежний статус: ")
        if choice in valid_statuses:
            note["status"] = valid_statuses[choice]  # Обновление статуса
            print("Статус заметки успешно обновлён на:", note["status"])
            break
        elif choice == "":
            break  # Выход из цикла, если пользователь оставил строку пустой
        else:
            print("Некорректный ввод. Пожалуйста, выберите номер \
из предложенных вариантов.")


# Функция проверки дедлайна
def check_deadline(note):
    current_date = datetime.now()  # Получение текущей даты
    print(f"Текущая дата: {current_date.strftime('%d-%m-%Y')}")
    while True:
        try:
            deadline = datetime.strptime(note["issue_date"], "%d-%m-%Y")
            days_left = (deadline - current_date).days  # дней до дедлайна

            if days_left < 0:
                print(f"Внимание! Дедлайн истёк {abs(days_left)} дня(ей) \
назад.")
            elif days_left == 0:
                print("Дедлайн сегодня!")
            else:
                print(f"До дедлайна осталось {days_left} дня(ей).")
            break
        except ValueError:
            print("Некорректный формат даты. Пожалуйста, используйте \
формат 'ДД-ММ-ГГГГ'.")


# Функция для отображения всех заметок
def display_notes():
    print("\nСписок заметок:")
    if not notes:
        print("Нет доступных заметок.")
        return
    # Перебор всех заметок в списке
    for i, note in enumerate(notes, start=1):
        print(f"\nЗаметка номер {i}:")
        print("Имя пользователя:", note["username"])
        print("Заголовки заметки:")
        # Перебор заголовков заметки
        for j, title in enumerate(note["titles"], start=1):
            print(f'- Заголовок заметки номер {j}: {title}')
        print("Описание заметки:", note["content"])
        print("Статус заметки:", note["status"])
        print('Дата создания заметки:', note['created_date'])
        print('Дата истечения заметки:', note['issue_date'])
        check_deadline(note)  # Проверка дедлайна для каждой заметки


# Функция для удаления заметок
def delete_notes():
    while True:  # Цикл для повторного запроса выбора критерия
        print("Выберите критерий для удаления заметок:")
        print("1. По имени пользователя")
        print("2. По заголовку заметки")

        criterion = input("Введите номер пункта (1 или 2): ").strip()
        if criterion not in ['1', '2']:
            print("Некорректный ввод. Пожалуйста, введите '1' или '2'.")
            continue  # Запросить ввод снова, если введено некорректно

        if criterion == '1':
            value = input("Введите имя пользователя для \
удаления заметок: ").strip()
        elif criterion == '2':
            value = input("Введите заголовок заметки для удаления: ").strip()

        if not value:
            print("Вы не ввели значение. Пожалуйста, попробуйте снова.")
            continue  # Запросить ввод снова, если значение пустое

        initial_count = len(notes)

        # Удаляем заметки по критерию
        if criterion == '1':
            notes[:] = [note for note in notes if note['username'] != value]
        elif criterion == '2':
            notes[:] = [note for note in notes if value not in note['titles']]

        # Проверка, были ли удалены заметки
        if len(notes) < initial_count:
            print(f"Заметки с именем пользователя '{value}' успешно \
удалены." if criterion == '1' else f"Заметки \
с заголовком '{value}' успешно удалены.")
        else:
            print(f"Заметки с именем пользователя '{value}' не \
найдены." if criterion == '1' else f"Заметки с \
заголовком '{value}' не найдены.")

        # Вывод оставшихся заметок
        if initial_count - len(notes) > 0:
            display_notes()
        break


# Основная функция для запуска программы
def main():
    print("Добро пожаловать в 'Менеджер заметок'! Вы можете \
добавить новую заметку.")
    while True:
        create_note()  # Вызов функции для создания заметки
        if not confirm("Хотите добавить ещё одну заметку? (да/нет): "):
            break

    display_notes()  # Вывод всех заметок после завершения ввода

    while confirm("Хотите удалить заметки? (да/нет): "):
        delete_notes()  # Вызов функции для удаления заметок

# Запуск основной функции


main()
