# Создаем словарь для хранения данных заметки
note = {}

# Запрашиваем у пользователя текущий статус заметки
note["status"] = input("Введите текущий статус заметки (например, 'в процессе', 'выполнено', 'отложено'): ")


# Функция для отображения списка доступных статусов
def display_status_options():
    print("\nВыберите новый статус заметки:")
    print("1. Выполнено")
    print("2. В процессе")
    print("3. Отложено")


# Функция для обновления статуса
def update_note_status():
    valid_statuses = {
        "1": "выполнено",
        "2": "в процессе",
        "3": "отложено"
    }

    while True:
        display_status_options()
        choice = input("Ваш выбор (введите номер статуса): ")

        # Проверяем корректность ввода
        if choice in valid_statuses:
            note["status"] = valid_statuses[choice]
            print("Статус заметки успешно обновлён на:", note["status"])
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите номер из предложенных вариантов.")


# Вызываем функцию для обновления статуса
update_note_status()


# Дополнительная функциональность: проверка дедлайна
def check_deadline(issue_date):
    from datetime import datetime

    # Преобразуем строку даты в объект datetime
    try:
        deadline = datetime.strptime(issue_date, "%d-%m-%Y")
        if deadline < datetime.now():
            print("Предупреждение: срок выполнения заметки истек!")
        else:
            print("Срок выполнения заметки еще не истек.")
    except ValueError:
        print("Некорректный формат даты. Пожалуйста, используйте формат 'день-месяц-год'.")


# Запрашиваем дату истечения заметки
note["issue_date"] = input("Введите дату истечения заметки в формате 'день-месяц-год': ")
check_deadline(note["issue_date"])
