import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Убедитесь, что aqa-shop запущен на порту 8080
BASE_UI_URL = "http://localhost:8080"

@allure.title("UI: Покупка тура с APPROVED картой")
@allure.description("Заполняем форму с валидной картой, проверяем успех")
def test_ui_payment_approved():
    driver = webdriver.Chrome()
    try:
        with allure.step("Открытие страницы покупки"):
            driver.get(BASE_UI_URL)
        with allure.step("Заполнение номера карты"):
            driver.find_element(By.NAME, "cardNumber").send_keys("4444 4444 4444 4441")
        with allure.step("Заполнение других полей"):
            driver.find_element(By.NAME, "month").send_keys("12")
            driver.find_element(By.NAME, "year").send_keys("25")
            driver.find_element(By.NAME, "cvv").send_keys("123")
        with allure.step("Отправка формы"):
            driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        with allure.step("Проверка сообщения об успехе"):
            success_message = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "success"))
            )
            assert "успешно" in success_message.text
    finally:
        driver.quit()

@allure.title("UI: Покупка тура с DECLINED картой")
@allure.description("Заполняем форму с невалидной картой, проверяем отказ")
def test_ui_payment_declined():
    driver = webdriver.Chrome()
    try:
        with allure.step("Открытие страницы покупки"):
            driver.get(BASE_UI_URL)
        with allure.step("Заполнение номера карты"):
            driver.find_element(By.NAME, "cardNumber").send_keys("4444 4444 4444 4442")
        with allure.step("Заполнение других полей"):
            driver.find_element(By.NAME, "month").send_keys("12")
            driver.find_element(By.NAME, "year").send_keys("25")
            driver.find_element(By.NAME, "cvv").send_keys("123")
        with allure.step("Отправка формы"):
            driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        with allure.step("Проверка сообщения об ошибке"):
            error_message = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "error"))
            )
            assert "отклонен" in error_message.text
    finally:
        driver.quit()