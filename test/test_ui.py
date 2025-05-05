import pytest
import allure
from selenium import webdriver
from page.ui import Delivui
from selenium.webdriver.common.by import By


@pytest.fixture()
@allure.title("инициализация драйвера")
@allure.description(
    "Эта функция Инициализирует драйвер"
    "и открывает окно браузера на весь экран в режиме инкогнито,"
    "убирает геолокацию из браузера."
    "Затем получает URL, создает генератор,"
    "которые позволяют итерировать через последовательность данных,"
    "и закрывает браузер.")
@allure.feature("инициализация драйвера")
@allure.severity("blocker")
def driver():
    with allure.step("драйвер"):
        options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.geolocation": 2}
        options.add_experimental_option("prefs", prefs)
        options.add_argument("--incognito")
        driver = webdriver.Chrome(options=options)
        driver.get("https://market-delivery.yandex.ru/")
        driver.maximize_window()
        yield driver
        driver.quit()


@allure.title("Выбор ресторана")
@allure.description(
    "Вызывает функцию, ставит неявное ожидание,"
    "вызывает класс, вызывает фунцию выбора адреса"
    "и выбора ресторана из класса")
@allure.feature("Выбор ресторана")
@allure.severity("blocker")
def test_choice_rest(driver):
    with allure.step("неявное ожидание"):
        driver.implicitly_wait(2)
    with allure.step("класс"):
        delivery = Delivui(driver)
    with allure.step("выбор адреса"):
        delivery.choice_add()
    with allure.step("выбор ресторана"):
        delivery.choice_rest()

    with allure.step("проверяем ресторан"):
        content = driver.find_element(
            By.CLASS_NAME,
            'nccn02t.UiKitText_root.UiKitText_HeaderLoose.UiKitText_Bold.UiKitText_Text'
            ).text
        assert content == "Вкусно – и точка"


@allure.title("Выбор товара")
@allure.description(
    "Вызывает функцию, ставит неявное ожидание, вызывает класс,"
    "вызывает фунцию выбора адреса, выбора ресторана"
    "и выбора товара из класса")
@allure.feature("Выбор товара")
@allure.severity("blocker")
def test_choice_prod(driver):
    with allure.step("неявное ожидание"):
        driver.implicitly_wait(2)
    with allure.step("класс"):
        delivery = Delivui(driver)
    with allure.step("выбор адреса"):
        delivery.choice_add()
    with allure.step("выбор ресторана"):
        delivery.choice_rest()
    with allure.step("выбор товара"):
        delivery.choice_prod()

    with allure.step("проверяем товар"):
        content = driver.find_element(By.CLASS_NAME, 'cllwzwr').text
        assert content == "Пирожок Вишневый"


@allure.title("Добавление товара в корзину")
@allure.description(
    "Вызывает функцию, ставит неявное ожидание, вызывает класс,"
    "вызывает фунцию выбора адреса, выбора ресторана"
    "и выбора товара из класса. Затем добавляет товар в корзину.")
@allure.feature("Добавление товара в корзину")
@allure.severity("blocker")
def test_add_to_cart(driver):
    with allure.step("неявное ожидание"):
        driver.implicitly_wait(2)
    with allure.step("класс"):
        delivery = Delivui(driver)
    with allure.step("выбор адреса"):
        delivery.choice_add()
    with allure.step("выбор ресторана"):
        delivery.choice_rest()
    with allure.step("выбор товара"):
        delivery.choice_prod()
    with allure.step("добавление товара"):
        delivery.add_to_cart()

    with allure.step("проверяем количество"):
        content = driver.find_element(By.CLASS_NAME, 'v15609t0').text
        assert content == "1"


@allure.title("Добавление еще одного такого же товара в корзину")
@allure.description(
    "Вызывает функцию, ставит неявное ожидание, вызывает класс,"
    "вызывает фунцию выбора адреса, выбора ресторана"
    "и выбора товара из класса и добавляет товар в корзину."
    "Затем добавляет еще один так же товар.")
@allure.feature("Добавление еще одного такого же товара в корзину")
@allure.severity("blocker")
def test_add_more_to_cart(driver):
    with allure.step("неявное ожидание"):
        driver.implicitly_wait(2)
    with allure.step("класс"):
        delivery = Delivui(driver)
    with allure.step("выбор адреса"):
        delivery.choice_add()
    with allure.step("выбор ресторана"):
        delivery.choice_rest()
    with allure.step("выбор товара"):
        delivery.choice_prod()
    with allure.step("добавление товара"):
        delivery.add_to_cart()
    with allure.step("добавление еще одного товара"):
        delivery.add_more_prod()

    with allure.step("проверяем количество"):
        content = driver.find_element(By.CLASS_NAME, 'v15609t0').text
        assert content == "2"


@allure.title("Удаление корзины")
@allure.description(
    "Вызывает функцию, ставит неявное ожидание, вызывает класс,"
    "вызывает фунцию выбора адреса, выбора ресторана"
    "и выбора товара из класса и добавляет товар в корзину,"
    "потом добавляет еще один такой же товар."
    "Затем удаляет корзину.")
@allure.feature("Удаление корзины")
@allure.severity("blocker")
def test_delete_to_cart(driver):
    with allure.step("неявное ожидание"):
        driver.implicitly_wait(2)
    with allure.step("класс"):
        delivery = Delivui(driver)
    with allure.step("выбор адреса"):
        delivery.choice_add()
    with allure.step("выбор ресторана"):
        delivery.choice_rest()
    with allure.step("выбор товара"):
        delivery.choice_prod()
    with allure.step("добавление товара"):
        delivery.add_to_cart()
    with allure.step("добавление еще одного товара"):
        delivery.add_more_prod()
    with allure.step("очистка корзины"):
        delivery.delete_to_cart()

    with allure.step("проверяем количество"):
        content = driver.find_element(
            By.CLASS_NAME,
            'NewCartEmpty_title.UiKitText_root.UiKitText_Title4.UiKitText_Bold.UiKitText_Text'
            ).text
        assert content == "В вашей корзине \nпока пусто"
