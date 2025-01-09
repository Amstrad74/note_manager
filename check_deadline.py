from datetime import datetime

# Создали словарь для хранения данных заметки
note = {}


# Функция проверки дедлайна
def check_deadline():
    # Получаем текущую дату
    current_date = datetime.now()
    print(f"Текущая дата: {current_date.strftime('%d-%m-%Y')}")

    while True:
        # Запрашиваем у пользователя дату дедлайна
        note["issue_date"] = input("Введите дату истечения заметки в формате 'ДД-ММ-ГГГГ': ")

        try:
            # Преобразуем строку из словаря в объект datetime
            issue_date = datetime.strptime(note["issue_date"], "%d-%m-%Y")

            # Вычисляем разницу между текущей датой и дедлайном
            delta = (issue_date - current_date).days

            # Проверяем, истёк ли дедлайн
            if delta < 0:
                print(f"Предупреждение: срок выполнения заметки истек {abs(delta)} дня(ей) назад.")
            elif delta == 0:
                print("Сегодня последний день выполнения заметки.")
            else:
                print(f"До истечения срока выполнения заметки осталось {delta} дня(ей).")
            break  # Выход из цикла, если дата введена корректно

        except ValueError:
            print("Некорректный формат даты. Пожалуйста, используйте формат 'ДД-ММ-ГГГГ'.")


# Запускаем проверку дедлайна
check_deadline()
