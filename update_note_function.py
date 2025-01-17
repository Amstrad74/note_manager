# Импортируем необходимые модули для работы с датами
from datetime import datetime


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


# Функция обновления заметки
def update_note(note):

    # Опции для обновления
    fields = ['username', 'titles', 'content', 'status', 'issue_date']
    print("Какие данные вы хотите обновить? Выберите номера через \
запятую (например, 1,2):")

    for i, field in enumerate(fields, start=1):
        print(f"{i}. {field}")

    while True:
        selected_fields = input("Введите номера полей для \
обновления: ").strip().split(',')
        selected_fields = [
            s.strip() for s in selected_fields if s.strip().isdigit()
        ]

        if not selected_fields:
            print("Некорректный ввод. Пожалуйста, выберите хотя бы одно поле.")
            continue

        # Обновление выбранных полей
        for field_index in selected_fields:
            index = int(field_index) - 1
            if index < 0 or index >= len(fields):
                print(f"Некорректный номер поля: {field_index}. Пожалуйста, \
выберите номер от 1 до {len(fields)}.")
                continue

            field = fields[index]

            if field == 'titles':
                new_titles = []
                print("Введите новые заголовки заметки (оставьте пустым \
для завершения):")
                while True:
                    title = input("Введите заголовок заметки: ")
                    if title == "":
                        break  # Завершение ввода, если строка пустая
                    new_titles.append(title)  # Добавление заголовка
                note[field] = new_titles  # Обновление заголовков
            elif field == 'issue_date':
                note[field] = input_date("Введите новое значение \
для issue_date в формате 'ДД-ММ-ГГГГ': ")
            elif field == 'status':
                # Запрос статуса заметки с проверкой на корректный ввод
                while True:
                    status = input("Введите статус заметки (новая, \
в процессе, выполнено): ").strip().lower()
                    if status in ["новая", "в процессе", "выполнено"]:
                        note["status"] = status
                        break
                    else:
                        print("Некорректный статус. Пожалуйста, \
введите 'новая', 'в процессе' или 'выполнено'.")
            else:
                new_value = input(f"Введите новое значение для {field}: ")
                note[field] = new_value  # Обновление значения

        print("Заметка успешно обновлена!")
        return note  # Возврат обновленного словаря заметки


# Пример использования функции
def main():

    print("Текущие данные заметки:")  # Вывод текущей заметки
    print(note)
    updated_note = update_note(note)  # Вызов функции обновления заметки
    print("Обновленная заметка:", updated_note)  # Вывод обновленной заметки


# точка входа
if __name__ == "__main__":
    # Пример заметки
    note = {
        'username': 'Иван',
        'titles': ['Учеба', 'Спорт'],
        'content': 'Подготовиться к экзамену',
        'status': 'отложено',
        'created_date': '01-01-2025',
        'issue_date': '25-06-2025'
    }
    # Запуск основной функции
    main()
