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


# Функция для отображения всех заметок
def display_notes():
    if not notes:
        print("Нет доступных заметок.")
        return
    # Перебор всех заметок в списке
    for i, note in enumerate(notes, start=1):
        print(f"\nЗаметка номер {i}:")
        print("Имя пользователя:", note["username"])
        # Перебор заголовков заметки
        for j, title in enumerate(note["titles"], start=1):
            print(f'- Заголовок заметки номер {j}: {title}')
        print("Описание заметки:", note["content"])
        print("Статус заметки:", note["status"])
        print('Дата создания заметки:', note['created_date'])
        print('Дата истечения заметки:', note['issue_date'])


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
            # Нечувствительное к регистру сравнение для имени пользователя
            notes[:] = [
                note for note in notes
                if note['username'].lower() != value.lower()
            ]
        elif criterion == '2':
            # Нечувствительное к регистру сравнение для заголовков
            notes[:] = [
                note for note in notes
                if value.lower() not in [
                    title.lower() for title in note['titles']
                ]
            ]

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
            print("\nВот текущий список ваших заметок:")
            display_notes()
        break


# Основная функция для запуска программы
def main():
    print("Добро пожаловать в 'Менеджер заметок'!")
    print("\nСписок заметок:")

    display_notes()  # Вывод всех заметок после завершения ввода

    while confirm("\nХотите удалить заметки? (да/нет): "):
        if len(notes) > 0:
            delete_notes()  # Вызов функции для удаления заметок
        else:
            print("Нет заметок для удаления")

# Точка входа
if __name__ == "__main__":
    # Список для хранения всех заметок
    notes = [
        {
            'username': 'Вася',
            'titles': ['Список покупок'],
            'content': 'Купить продукты на неделю',
            'status': 'в процессе',
            'created_date': '12-01-2025',
            'issue_date': '13-02-2025'
        },
        {
            'username': 'Иван',
            'titles': ['Учеба', 'Спорт'],
            'content': 'Подготовиться к экзамену',
            'status': 'отложено',
            'created_date': '01-01-2025',
            'issue_date': '25-06-2025'
        }
    ]

    # Запуск основной функции
    main()
