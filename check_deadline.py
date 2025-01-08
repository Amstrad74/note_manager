# Обработка дедлайнов

from datetime import datetime

# Функция для проверки дедлайна
def check_deadline(issue_date):
    try:
        # Преобразуем строку даты в объект datetime
        deadline = datetime.strptime(issue_date, "%d-%m-%Y")
        if deadline < datetime.now():
            print("Предупреждение: срок выполнения заметки истек!")
        else:
            print("Срок выполнения заметки еще не истек.")
    except ValueError:
        print("Некорректный формат даты. Пожалуйста, используйте формат 'день-месяц-год'.")

# Запрашиваем дату истечения заметки у пользователя
issue_date = input("Введите дату истечения заметки в формате 'день-месяц-год': ")

# Вызываем функцию проверки дедлайна
check_deadline(issue_date)
