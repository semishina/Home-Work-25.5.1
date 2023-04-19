import pytest
from settings import email, password, url
from selenium.webdriver.common.by import By
from selenium import webdriver


@pytest.fixture()
def browser():
    """Инициализируем браузер и закрываем его после тестов"""
    driver = webdriver.Chrome()  # инициализируем браузер
    yield driver
    driver.quit()  # закрываем браузер

@pytest.fixture(autouse=True)
def login(browser):
    """Вводим валидные данные зарегистрированного пользователя и нажимаем кнопку войти"""
    browser.implicitly_wait(10)
    # закладываем время на неявное ожидание не дольше 10 секунд

    browser.get(url)
    btn_new_user = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-success")
    btn_new_user.click()
    # Открываем страницу регистрации, находим по локатору кнопку "Регистрация" и нажимаем ее.

    btn_exist_acc = browser.find_element(By.CSS_SELECTOR, "a[href='/login']")
    btn_exist_acc.click()
    # Находим по локатору кнопку "у меня уже есть аккаунт" и нажимаем ее.

    field_email = browser.find_element(By.ID, "email")
    field_email.clear()
    field_email.send_keys(email)
    # вводим email, предварительно очистив поле ввода

    field_pass = browser.find_element(By.ID, "pass")
    field_pass.clear()
    field_pass.send_keys(password)
    # вводим пароль, предварительно очистив поле ввода

    btn_submit = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    btn_submit.click()
    # Находим по локатору кнопку "войти" и нажимаем ее.

    result = browser.find_element(By.CSS_SELECTOR, 'h1').text
    return result


