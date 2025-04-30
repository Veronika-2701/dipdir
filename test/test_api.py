import pytest
import allure
import json
from page.api import Delivery

ratata = Delivery("https://market-delivery.yandex.ru/")


@pytest.fixture()
@allure.title("Добавление в корзину товара")
@allure.description("Вызывает функцию,"
    "в которой валидный Request на методе Post.")
@allure.feature("Добавление в корзину товара")
@allure.severity("blocker")
def test_val_add_to_cart():
    with allure.step("Request"):
        PROJ_RESP = ratata.req_post(
            'POST',
            'api/v1/cart?longitude=36.'
            '596940017230644&latitude=55.11887434865486',
            {"item_id": 2012980624,
             "quantity": 2,
             "place_slug": "vkusno__i_tochka_srtfo",
             "place_business": "restaurant",
             "item_options": []
             }
            )
    with allure.step("Сравниваем, что в ответе код 200"):
        assert PROJ_RESP.status_code == 200


@allure.title(
        "При добавлении в корзину определенного товара,"
        "товар корректно отображается в корзине")
@allure.description(
        "Вызывает функцию,"
        "в которой валидный Request на методе Post.")
@allure.feature(
        "При добавлении в корзину определенного товара,"
        "товар корректно отображается в корзине")
@allure.severity("blocker")
def test_val_add_to_cart2():
    with allure.step("Request"):
        PROJ_RESP = ratata.req_post(
            'POST',
            'api/v1/cart?longitude=36.'
            '596940017230644&latitude=55.11887434865486',
            {"item_id": 2012980624,
             "quantity": 3,
             "place_slug": "vkusno__i_tochka_srtfo",
             "place_business": "restaurant",
             "item_options": []
             }
            )
    with allure.step(
        "Сравниваем, что название Двойной чизбургер есть в ответе"
            ):
        resp = PROJ_RESP.text
        name = "Двойной Чизбургер"
        assert name in resp
    with allure.step("Сравниваем, что в ответе код 200"):
        assert PROJ_RESP.status_code == 200
    with allure.step(
        "Сравниваем, что название Двойной чизбургер есть в ответе"
            ):
        js = json.loads(PROJ_RESP.text)
        tr = js["cart"]["items"][0]["name"]
        assert tr == "Двойной Чизбургер"


@allure.title(
        "Добавление товара в корзину из другого ресторана,"
        "когда уже создана корзина на предыдущий ресторан")
@allure.description(
        "Вызывает функцию,"
        "в которой сначала создаем корзину на один магазин,"
        "потом на другой и проверяем, что первой корзины больше нет")
@allure.feature(
        "Добавление товара в корзину из другого ресторана,"
        "когда уже создана корзина на предыдущий ресторан")
@allure.severity("blocker")
def test_val_add_to_cart3():
    with allure.step("Request1"):
        PROJ_RESP = ratata.req_post(
            'POST',
            'api/v1/cart?longitude=37.'
            '35881951562494&latitude=55.64320912230436',
            {"item_id": 2090633917,
             "quantity": 1,
             "place_slug": "burger_king_awyvd",
             "place_business": "restaurant",
             "item_options": []
             }
            )
    with allure.step("Request2"):
        PROJ_RESP2 = ratata.req_post(
            'POST',
            'api/v1/cart?longitude=37.'
            '35881951562494&latitude=55.64320912230436',
            {"item_id": 1512201284,
             "quantity": 1,
             "place_slug": "tanuki_psmhn",
             "place_business": "restaurant",
             "item_options": []
             }
            )
    with allure.step("Сравниваем, что код 400 на первую корзину"):
        assert PROJ_RESP.status_code == 400
    with allure.step("Сравниваем, что код 200 на вторую корзину"):
        assert PROJ_RESP2.status_code == 200
    with allure.step("Проверяем, что корзина на второй ресторан не доступна"):
        js = json.loads(PROJ_RESP.text)
        tr = js["err"]
        assert tr == "Ресторан недоступен"


@allure.title("Добавление товара в корзину"
              "с неправильно написанным названием магазина")
@allure.description("Вызывает функцию и проверяем на невалидные проверки")
@allure.feature("Добавление товара в корзину"
                "с неправильно написанным названием магазина")
@allure.severity("blocker")
def test_inval_add_to_cart4():
    with allure.step("Request"):
        PROJ_RESP = ratata.req_post(
            'POST',
            'api/v1/cart?longitude=36.'
            '596940017230644&latitude=55.11887434865486',
            {"item_id": 2012980624,
             "quantity": 3,
             "place_slug": "vkusno__i_tochka",
             "place_business": "restaurant",
             "item_options": []
             }
            )
    with allure.step("Сравниваем, что код 400 возвращается"):
        assert PROJ_RESP.status_code == 400


@allure.title("Добавление товара в корзину с несуществующем id")
@allure.description("Вызывает функцию и проверяет на невалидную проверку.")
@allure.feature("Добавление товара в корзину с несуществующем id")
@allure.severity("blocker")
def test_add_to_cart5():
    with allure.step("Request"):
        PROJ_RESP = ratata.req_post(
            'POST',
            'api/v1/cart?longitude=36.'
            '596940017230644&latitude=55.11887434865486',
            {"item_id": 3014789034,
             "quantity": 1,
             "place_slug": "vkusno__i_tochka_vdxwa",
             "place_business": "restaurant",
             "item_options": []
             }
            )
    with allure.step("Сравниваем, что код 400 возвращается"):
        assert PROJ_RESP.status_code == 400
