import sqlite3


def clear_database():
    # Путь к файлу вашей базы данных
    db_path = 'tests_db.sqlite'

    # Соединение с базой данных
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Список таблиц для очистки
    tables_to_clear = ['questions', 'tests']

    try:
        for table in tables_to_clear:
            # Формирование SQL-запроса для очистки таблицы
            query = f'DELETE FROM {table};'
            cursor.execute(query)
            print(f"Таблица {table} успешно очищена.")

        # Сброс AUTOINCREMENT значений для очищенных таблиц
        cursor.execute("DELETE FROM sqlite_sequence WHERE name IN ('" + "','".join(tables_to_clear) + "');")
        print("Значения AUTOINCREMENT успешно сброшены.")

        conn.commit()
    except sqlite3.Error as e:
        print(f"Ошибка при очистке базы данных: {e}")
    finally:
        # Закрытие соединения с базой данных
        conn.close()


if __name__ == "__main__":
    clear_database()
