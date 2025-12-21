import allure
import mysql.connector

# Убедитесь, что mysql запущен на порту 3306
DB_CONFIG = {
    'host': 'localhost',  # или 'mysql' в CI
    'port': 3306,
    'user': 'app',
    'password': 'app',
    'database': 'app'
}

@allure.title("DB: Проверка записи транзакции в БД")
@allure.description("Проверяем, что после покупки транзакция сохранена в таблицу")
def test_transaction_saved():
    with allure.step("Подключение к БД"):
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor()

    with allure.step("Запрос последней транзакции"):
        cursor.execute("SELECT status FROM transactions ORDER BY id DESC LIMIT 1;")
        result = cursor.fetchone()

    with allure.step("Проверка, что статус в списке"):
        assert result[0] in ["APPROVED", "DECLINED"]

    cursor.close()
    connection.close()

@allure.title("DB: Проверка количества транзакций")
@allure.description("Проверяем, что после покупки количество транзакций увеличилось")
def test_transaction_count():
    with allure.step("Подключение к БД"):
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor()

    with allure.step("Счётчик транзакций до"):
        cursor.execute("SELECT COUNT(*) FROM transactions;")
        count_before = cursor.fetchone()[0]

    # Здесь можно выполнить покупку через API или UI (если тест интеграционный)

    with allure.step("Счётчик транзакций после"):
        cursor.execute("SELECT COUNT(*) FROM transactions;")
        count_after = cursor.fetchone()[0]

    with allure.step("Проверка, что количество увеличилось"):
        assert count_after > count_before

    cursor.close()
    connection.close()