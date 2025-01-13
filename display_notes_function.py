# Импортируем необходимые модули
from colorama import Fore, Style, init

# Инициализация colorama
init(autoreset=True)

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
    }
]

# Функция для отображения всех заметок
def display_notes():
    print(Fore.CYAN + "\nСписок заметок:" + Style.RESET_ALL)
    for i, note in enumerate(notes, start=1):  # Перебор всех заметок в списке
        print(Fore.YELLOW + "---------------" + Style.RESET_ALL)
        print(Style.BRIGHT + Fore.GREEN + f"Заметка №{i}:" + Style.RESET_ALL)
        print(Fore.LIGHTWHITE_EX + "Имя пользователя: " + Style.BRIGHT + Fore.WHITE + note["username"])
        print(Fore.LIGHTWHITE_EX + "Заголовки заметки:")
        # Перебор заголовков заметки
        for j, title in enumerate(note["titles"], start=1):
            print(Fore.LIGHTWHITE_EX + f'- Заголовок заметки № {j}: {Style.BRIGHT + Fore.WHITE}{title}')
        print(Fore.LIGHTWHITE_EX + "Описание заметки: " + Style.BRIGHT + Fore.WHITE + note["content"])
        print(Fore.LIGHTWHITE_EX + "Статус заметки: " + Style.BRIGHT + Fore.WHITE + note["status"])
        print(Fore.LIGHTWHITE_EX + 'Дата создания заметки: ' + Style.BRIGHT + Fore.WHITE + note['created_date'])
        print(Fore.LIGHTWHITE_EX + 'Дедлайн: ' + Style.BRIGHT + Fore.WHITE + note['issue_date'])

# Основная функция для запуска программы
def main():
    print(Fore.CYAN + "Добро пожаловать в 'Менеджер заметок'!" + Style.RESET_ALL)
    display_notes()  # Вывод всех заметок после завершения ввода
    print(Fore.YELLOW + "---------------" + Style.RESET_ALL)

# Запуск основной функции
main()
