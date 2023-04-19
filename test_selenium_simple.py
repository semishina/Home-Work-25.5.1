from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_petfriends_authorization(browser):
    """Проверяем успешность авторизации"""
    result = browser.find_element(By.CSS_SELECTOR, 'h1').text
    assert result == "PetFriends", "login error"

def test_petfriends_pets_cards(browser):
    """Проверяем наличие всех элементов карточек питомцев: объявляем три переменные,
    в которые записываем все найденные по локаторам элементы на странице:
    в images — все картинки питомцев, в names — все их имена, в descriptions — все виды и возрасты.
    Далее организуем цикл, который может перебрать все эти элементы.  """

    images = browser.find_elements(By.CSS_SELECTOR, '.card-deck .card-img-top')
    names = browser.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')
    descriptions = browser.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')

    for i in range(len(names)):
        assert images[i].get_attribute('src') != '', 'Image not found'
        assert names[i].text != '', 'Name not found'
        assert descriptions[i].text != '', 'Description not found'
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0, 'Species not found'
        assert len(parts[1]) > 0, 'Age not found'
        #Убеждаемся, что в данном элементе выводится и возраст, и вид питомца:
        # ищем в тексте этого элемента запятую, так как считаем её разделителем между этими двумя сущностями.
        # Чтобы убедиться, что в строке есть и возраст питомца, и его вид, мы разделяем строку по запятой
        # и ждём, что каждая из частей будет длиной больше нуля, а, значит, содержит и вид, и возраст питомца.


def test_petfriends_card_deck(browser):
    """Проверяем наличие всех элементов страницы с помощью поиска по локаторам.
        Для уверенности в том, что элемент точно загрузился,
        задаем время его ожидания не меньше 10 секунд. Явное ожидание."""

    # Проверка наличия таблицы с питомцами методом "Ожидание присутствия элемента в структуре документа"
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.card-deck')))

    # Проверка наличия видимости элементов на странице методом "Ожидание видимости элемента на экране".
    # Наличие центральных надписей "PetFriends" и "Все питомцы наших пользователей"
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'h1.text-center')))
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR,'div.text-center:nth-child(2)')))

    # наличие панели навигации
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, 'navbarNav')))

    # наличие кнопок "PetFriends", "Мои питомцы", "Все питомцы", "Выйти"
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'a.navbar-brand.header2')))
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/my_pets"]')))
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/all_pets"]')))
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'button.btn.btn-outline-secondary')))

    assert  browser.current_url == 'https://petfriends.skillfactory.ru/all_pets', "login error"

