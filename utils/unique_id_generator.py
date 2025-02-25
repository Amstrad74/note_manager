import uuid  # Импорт модуля uuid для генерации уникальных идентификаторов


# Генерирует уникальный идентификатор.
def generate_unique_id():
    # Генерация уникального идентификатора с использованием UUID4
    unique_id = uuid.uuid4()
    # Преобразование UUID в строку для удобства использования и возврата
    return str(unique_id)


# Точка входа
if __name__ == "__main__":
    print("Тест uuid\n", generate_unique_id())