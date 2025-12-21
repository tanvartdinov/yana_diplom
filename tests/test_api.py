import requests
import allure

# Убедитесь, что gate-simulator запущен на порту 9999
BASE_GATE_URL = "http://localhost:9999"  # или "http://gate-simulator:9999" в CI

@allure.title("API: Покупка тура с APPROVED картой")
@allure.description("Отправляем данные карты 4444 4444 4444 4441, ожидаем APPROVED")
def test_payment_approved():
    payload = {"number": "4444 4444 4444 4441"}
    with allure.step("Отправка POST-запроса на /payment"):
        response = requests.post(f"{BASE_GATE_URL}/payment", json=payload)
    with allure.step("Проверка статуса 200"):
        assert response.status_code == 200
    with allure.step("Проверка ответа APPROVED"):
        assert response.json()["status"] == "APPROVED"

@allure.title("API: Покупка тура с DECLINED картой")
@allure.description("Отправляем данные карты 4444 4444 4444 4442, ожидаем DECLINED")
def test_payment_declined():
    payload = {"number": "4444 4444 4444 4442"}
    with allure.step("Отправка POST-запроса на /payment"):
        response = requests.post(f"{BASE_GATE_URL}/payment", json=payload)
    with allure.step("Проверка статуса 200"):
        assert response.status_code == 200
    with allure.step("Проверка ответа DECLINED"):
        assert response.json()["status"] == "DECLINED"

@allure.title("API: Кредит с APPROVED картой")
@allure.description("Отправляем данные карты 4444 4444 4444 4441 на /credit, ожидаем APPROVED")
def test_credit_approved():
    payload = {"number": "4444 4444 4444 4441"}
    with allure.step("Отправка POST-запроса на /credit"):
        response = requests.post(f"{BASE_GATE_URL}/credit", json=payload)
    with allure.step("Проверка статуса 200"):
        assert response.status_code == 200
    with allure.step("Проверка ответа APPROVED"):
        assert response.json()["status"] == "APPROVED"

@allure.title("API: Кредит с DECLINED картой")
@allure.description("Отправляем данные карты 4444 4444 4444 4442 на /credit, ожидаем DECLINED")
def test_credit_declined():
    payload = {"number": "4444 4444 4444 4442"}
    with allure.step("Отправка POST-запроса на /credit"):
        response = requests.post(f"{BASE_GATE_URL}/credit", json=payload)
    with allure.step("Проверка статуса 200"):
        assert response.status_code == 200
    with allure.step("Проверка ответа DECLINED"):
        assert response.json()["status"] == "DECLINED"