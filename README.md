# note_manager
## Grade 1. Этап 1

**greetings.py** 
(Задание 1) Основные переменные. 
Созданы базовые переменные для заметки: username, title, content, status, 
created_date, issue_date. 
Вывод значений организован через print.

**lesson_07.py**
Практическое задание к лекции "Функция ввода и работа с отладчиком".
Запрашивает у пользователя его имя и возраст.
Выводит сообщение о том, сколько лет исполнится пользователю через 5 лет.


**date_changer.py**
(Задание 2) Изменение формата вывода даты.
Реализовано преобразование формата отображения дат для пользователя, исключив 
год при выводе переменных created_date и issue_date.


**add_input.py**
(Задание 3) Ввод данных через input.
Переменные инициализируются через пользовательский ввод (input).
Реализованы подсказки для пользователя о том, как вводить данные, включая формат дат.
Вывод даты изменен - не выводится год.

**add_list.py**
(Задание 4) Добавление списка заголовков.
Пользователь вводит три заголовка через input(), которые сохраняются в список. 
Введенные данные отображаются, включая список заголовков.
Вывод даты изменен - не выводится год.

**final.py**
(Задание 5) Использование словаря.
Все данные организованы в словарь для заметки note{}, включая:
Поля: username, content, status, created_date, issue_date. 
Список заголовков как значение ключа titles. 
Все данные выводятся на экран в структурированном виде.
Ввод данных пользователем через input(), вывод через print()
Вывод даты изменен - не выводится год.

## Grade 1. Этап 2

**add_titles_loop.py** Задание 1.
Используя цикл запрашивает заголовки у пользователя и позволяет завершить 
ввод пустым вводом. Проводится проверка на уникальность заголовка.
Все данные организованы в словарь для заметки note.
Список заголовков как значение ключа titles. 
Вывод даты изменен - не выводится год.

**update_status.py** Задание 2. 
Запрашивает у пользователя текущий статус заметки и отображает его.
Предлагает пользователю изменить статус заметки, показывая список 
возможных статусов перед вводом.
Проверяет корректность введённого значения статуса. 
Если пользователь вводит некорректное значение, запрос повторяется.
В конце программа выводит все данные в структурированном виде.
Вывод даты изменен - не выводится год.

**check_deadline.py** Задание 3.
Сравнивает дату дедлайна заметки (issue_date) с текущей датой.
Выводит соответствующее сообщение:
Если дедлайн истёк, предупреждает пользователя.
Если дедлайн не истёк, сообщает, сколько времени осталось до истечения срока.

**multiple_notes.py** Задание 4.
Реализует возможность создания и хранения нескольких заметок в списке.
Используя цикл запрашивает заголовки у пользователя и позволяет завершить 
ввод пустым вводом. Проводится проверка на уникальность заголовка.
Обновляет статус заметки, с проверкой на корректное значение.
Вводит дату создания и истечения заметки с проверкой на дату.
Проверяет дедлайн. После этого выводит в структурированном виде данные заметок.

**delete_note.py**
Реализует возможность создания и хранения нескольких заметок в списке.
Используя цикл запрашивает заголовки у пользователя и позволяет завершить 
ввод пустым вводом. Проводится проверка на уникальность заголовка.
Обновляет статус заметки, с проверкой на корректное значение.
Вводит дату создания и истечения заметки с проверкой на дату.
Проверяет дедлайн. После этого выводит в структурированном виде данные заметок.
Удаляет заметку из списка по имени пользователя или заголовку.
Выводит сообщение, если заметка не найдена.
Обновляет список заметок.