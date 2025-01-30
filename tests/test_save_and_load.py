import unittest  # Импорт модуля unittest для создания и запуска тестов

# Импорт функций для сохранения и загрузки заметок из модуля note_manager.data
from note_manager.data.saver_notes_json import save_notes_json
from note_manager.data.loader_notes_from_file import load_notes_from_file


# Класс для тестирования функциональности управления заметками.
class TestNoteManager(unittest.TestCase):


    def test_save_and_load_notes(self):
        # Создание тестового списка заметок
        notes = [{'username': 'Test name', 'title': 'Test Note'}]
        # Сохранение тестовых заметок в файл 'test.json'
        # с помощью функции save_notes_json
        save_notes_json(notes, 'test.json')
        # Загрузка заметок из файла 'test.json'
        # с помощью функции load_notes_from_file
        loaded_notes = load_notes_from_file('test.json')
        # Проверка, что исходные заметки и загруженные заметки равны
        self.assertEqual(notes, loaded_notes)


# Точка входа в тестовый скрипт.
if __name__ == '__main__':
    unittest.main()  # Запуск тестов с помощью unittest
