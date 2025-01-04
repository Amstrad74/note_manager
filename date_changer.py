# Запрос информации
username = input("Введите имя пользователя: ")
content = input("Введите описание заметки: ")
status = input("Введите статус заметки (например, 'В работе', 'Выполнена'): ")
created_date = input("Введите дату создания заметки в формате 'день-месяц-год': ")
issue_date = input("Введите дату истечения заметки в формате 'день-месяц-год': ")

# Выводим все данные
print("\nВы ввели следующие данные:")
print("Имя пользователя:", username)
print("Описание заметки:", content)
print("Статус заметки:", status)

# Выводим дату без года.
temp_created_date = created_date.split(sep='-')
temp_issue_date = issue_date.split(sep='-')
print(f"Дата создания заметки: {temp_created_date[0]}-{temp_created_date[1]}")
print(f"Дата истечения заметки: {temp_issue_date[0]}-{temp_issue_date[1]}")
