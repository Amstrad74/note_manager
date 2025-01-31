def validate_status(status):
    return status in ["новая", "в процессе", "выполнена"]

# Точка входа
if __name__ == "__main__":
    status = "новая"
    print("Тест статуса\n", validate_status(status))