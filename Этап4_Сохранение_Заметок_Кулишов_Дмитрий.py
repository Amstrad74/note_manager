import yaml

# Функция для сохранения заметок в файл
def save_notes_to_file(notes, filename):
    # Открываем файл
    with open(filename, 'w', encoding='utf-8') as file:
        # Сохраняем заметки в формате YAML
        yaml.dump(notes, file, allow_unicode=True, sort_keys=False)

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
    save_notes_to_file(notes, 'notes.yaml')

# Точка входа
if __name__ == "__main__":
    main()
