# Импорт модуля datetime для работы с датами и временем
from datetime import datetime


# Проверяет, является ли строка допустимой датой в формате 'дд-мм-гггг'.
def validate_date(date_str):
    try:
        # Попытка преобразовать строку в объект datetime
        datetime.strptime(date_str, '%d-%m-%Y')
        # Если преобразование успешно, возвращаем True
        return True
    except ValueError:
        # Если возникает ошибка ValueError, это означает,
        # что строка не соответствует формату даты
        # Возвращаем False в этом случае
        return False

# Точка входа
if __name__ == "__main__":
    date_str = "01-01-2025"
    print("Тест даты\n", validate_date(date_str))