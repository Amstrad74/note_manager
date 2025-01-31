# note_manager
## Grade 1. Этап 1

в папке _stage1

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

в папке _stage2

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

**delete_note.py** Задание 5.
Проверяет дедлайн. После этого выводит в структурированном виде данные заметок.
Удаляет заметку из списка по имени пользователя или заголовку.
Выводит сообщение, если заметка не найдена.
Обновляет список заметок.

## Grade 1. Этап 3

в папке _stage3

**create_note_function.py** Задание 1.
Запрашивает у пользователя данные для создания заметки.
Автоматически добавляет текущую дату в поле created_date.
Формирует словарь с полями заметки.
Возвращает словарь.

**update_note_function.py** Задание 2.
Функция update_note() корректно принимает заметку в качестве аргумента.
Пользователь может выбрать поле для обновления.
Поле обновляется с учётом корректности введённого значения (например, проверка формата для даты).
Возвращается обновлённый словарь заметки.

**display_notes_function.py** Задание 3.
Принимает список заметок (каждая заметка — это словарь).
Нумерует заметки для удобства просмотра.
Выделяет каждый блок заметки горизонтальной чертой.
Отображает каждую заметку в в структурированном формате.
Если список заметок содержит больше 5 записей, происходит 
постраничный вывод. Реализована поддержка цветного вывода.

**search_notes_function.py** Задание 4.
Позволяет пользователю находить записи по ключевым словам или статусу.
Поиск с нечувствительностью к регистру, по нескольким ключевым словам.
Если указаны оба параметра (keyword и status), выполняет поиск 
с учётом обоих условий.
Результаты поиска выводятся в структурированном и читаемом формате.
Сообщения информируют пользователя, если заметки не найдены.

**menu.py** Задание 5.
Позволяет пользователю запускать различные функции (создание заметки, 
обновление, удаление и т.д.) через единый интерфейс.
Выводит интерактивное текстовое меню, позволяющее пользователю 
выбирать действия.
Выполняет выбранное пользователем действие, вызывая соответствующую функцию.
Повторно показывает меню после завершения действия, 
пока пользователь не выберет выход.
Если пользователь вводит недопустимый номер действия, программа выводит 
сообщение об ошибке и повторно показывает меню.

## Grade 1. Этап 4

В папке _stage4


## Grade 1. Этап 5
### **task1** Задание 1. Работа с модулями и пакетами.

Организуем проект так, чтобы его части (функции, данные, интерфейс) 
были разнесены по отдельным модулям.
Создаем следующие директории:
#### note_manager/
    ├── data/
    ├── utils/
    ├── interface/
    └── tests/

### **task2** Задание 2. Упрощение импорта через пакет.

Объединяем модули в пакеты, чтобы упростить импорт функций.
Например: from note_manager.data import save_notes
В каждом пакете (data, utils, interface) создаем __init__.py

### **task3** Задание 3. Рефакторинг функций в модули.

Переносим функции в соответствующие модули, чтобы каждая часть проекта 
содержала только связанные элементы.
#### Разделение функций
    * data/:
        ○	save_notes_to_file(), load_notes_from_file(), 
            append_notes_to_file(), save_notes_json().
    * utils/:
        ○	Валидация данных.
        ○	Генерация уникальных идентификаторов.
    * interface/:
        ○	Меню действий.
        ○	Отображение заметок.


### **task4** Задание 4. Создание тестов.

**test_note_manager.py**
Используем библиотеку unittest для написания тестов для проверки работы 
ключевых функций.
#### Проверяем:
    ○	Корректность сохранения и загрузки заметок.
    ○	Валидацию данных.
    ○	Отображение и поиск заметок.


### **task5** Задание 5. Создание вспомогательных утилит.

**date_validator.py**
Функция проверяет, соответствует ли дата формату "день-месяц-год".
Возвращает True, если дата корректна, иначе — False.

**status_validator**
Функция проверяет, что статус находится в списке допустимых значений 
(['новая', 'в процессе', 'выполнена']).
Возвращает True, если статус корректен, иначе — False.

**unique_id_generator.py**
Функция генерирует уникальный идентификатор для заметки.
