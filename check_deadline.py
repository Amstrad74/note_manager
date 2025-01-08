# Обработка дедлайнов


def check_deadline():

    from datetime import datetime

    # Запрашиваем дату истечения заметки у пользователя
    while True:
        issue_date = input(
            "Введите дату истечения заметки в \
формате 'ДД-ММ-ГГГГ': "
        )
        try:
            deadline = datetime.strptime(issue_date, "%d-%m-%Y")
            if deadline < datetime.now():
                print("Предупреждение: срок выполнения заметки истек!")
            else:
                print("Срок выполнения заметки еще не истек.")
            break  # Выход из цикла, если дата введена корректно
        except ValueError:
            print(
                "Некорректный формат даты. Пожалуйста, используйте \
формат 'ДД-ММ-ГГГГ'."
            )


# Запрашиваем дату истечения заметки и проверяем дедлайн
check_deadline()
