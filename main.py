# Импортируем необходимые модули
from colorama import Fore, Style
from interface.menu import menu


# Основная функция для запуска программы
def main(notes):
    print(
        Fore.CYAN + "Добро пожаловать в 'Менеджер заметок'!" + Style.RESET_ALL
    )
    menu(notes)


# Точка входа
if __name__ == "__main__":
    # Список заметок
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
        }
    ]

    main(notes)  # Запуск основной функции
