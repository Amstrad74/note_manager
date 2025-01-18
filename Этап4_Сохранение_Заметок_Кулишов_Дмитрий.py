# Функция для сохранения заметок в файл
def save_notes_to_file(notes, filename):
    file = open(filename, 'w', encoding='utf-8')  # Открываем файл
    try:
        for note in notes:
            file.write(f"Имя пользователя: {note['username']}\n")
            for title in note['titles']:
                file.write(f"Заголовок: {title}\n")
            file.write(f"Описание: {note['content']}\n")
            file.write(f"Статус: {note['status']}\n")
            file.write(f"Дата создания: {note['created_date']}\n")
            file.write(f"Дедлайн: {note['issue_date']}\n")
            file.write("-" * 20 + "\n")  # Разделитель между заметками
    finally:
        file.close()  # Закрываем файл


# Основная функция для запуска программы
def main():
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
        },
        {
            'username': 'Иван',
            'titles': ['Работа', 'Проект'],
            'content': 'Завершить проект к концу месяца',
            'status': 'новая',
            'created_date': '10-01-2025',
            'issue_date': '30-01-2025'
        }
    ]

    # Сохранение заметок в файл в формате YAML
    save_notes_to_file(notes, 'notes.txt')


# Точка входа
if __name__ == "__main__":
    main()
