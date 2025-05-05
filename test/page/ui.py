import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


@allure.epic("Деливери")
@allure.severity("blocker")
class Delivui:
    """Этот класс представляет сущность сайта Деливери."""
    @allure.id("инициализация Деливери")
    def __init__(self, driver):
        """Эта функция инициализует драйвер"""
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        driver.set_page_load_timeout(1)

    @allure.id("выбор адреса")
    def choice_add(self):
        """Эта функция находит элемент Адресса,
        ждет пока он прогрузится и станет кликабельным.
        Затем нажимает на него"""
        self.address_but = self.driver.find_element(
            By.CLASS_NAME, "r1jyb6b1.slw94yn.v102ekr4.syv67cr.w8m9n6r"
            )
        self.wait.until(EC.element_to_be_clickable(self.address_but)).click()
        """Эта функция ищет поле для Адресса,
        пишет в нее значение и нажимает Return."""
        self.input = self.driver.find_element(By.CSS_SELECTOR,
                                              ".afdxd29.mr7w3hr")
        self.input2 = self.input.send_keys("Обнинск, Курчатова 55")
        self.input3 = self.input.send_keys(Keys.RETURN)
        """Эта функция находит элемент кнопки ОК."""
        self.ok_but = self.driver.find_element(
            By.CSS_SELECTOR,
            ".r1jyb6b1.s1v4x2t8.v102ekr4.syv67cr.DesktopLocationModal_ok"
            ).click()

    @allure.id("выбор ресторана")
    def choice_rest(self):
        """Эта функция создает цикл,
        который скролит страницу и ищет нужный элемент,
        до того пока не найдет, затем закрывается."""
        while True:
            try:
                self.rest = self.driver.find_element(
                    By.XPATH, '//a[contains(@href,"vkusno__i_tochka")]'
                    )
                if self.rest:
                    self.rest.click()
                    break
            except NoSuchElementException:
                self.driver.find_element(
                    By.CSS_SELECTOR, "html"
                    ).send_keys(Keys.PAGE_DOWN)

    @allure.id("выбор товара")
    def choice_prod(self):
        """Эта функция создает цикл,
        который скролит страницу и ищет нужный элемент,
        до того пока не найдет, затем закрывается."""
        while True:
            try:
                self.prod = self.driver.find_element(
                    By.XPATH,
                    '//button[starts-with(@aria-label,"Пирожок Вишневый")]'
                    )
                if self.prod:
                    self.prod.click()
                    break
            except NoSuchElementException:
                self.driver.find_element(
                    By.CSS_SELECTOR, "html"
                    ).send_keys(Keys.PAGE_DOWN)

    @allure.id("добавление товара в корзину")
    def add_to_cart(self):
        """Эта функция находит кнопку,
        которая добавляет товар в корзину,
        и нажимает на нее."""
        self.cart = self.driver.find_element(
            By.CLASS_NAME, 'r1jyb6b1.slw94yn.v102ekr4.syv67cr.cwwswtx')
        self.cart.click()

    @allure.id("добавление такого же товара в корзину '+'")
    def add_more_prod(self):
        """Эта функция находит кнопку '+'
        и увеличивает количество товара в корзине"""
        self.more_prod = self.driver.find_element(
            By.XPATH, '//button[contains(@aria-label,"Увеличить")]')
        self.more_prod.click()

    @allure.id("удаление товара из корзины")
    def delete_to_cart(self):
        """Эта функция удаляет добавленный товар из корзины"""
        self.delete = self.driver.find_element(
            By.CLASS_NAME, 'r1jyb6b1.s5digsa.v1kdjjel.syv67cr.NewCart_clear')
        self.delete.click()
        self.del_yes = self.driver.find_element(
            By.CLASS_NAME,
            'r1orm7zp.st0n1t4.v102ekr4.shkwuuz.UiKitConfirmModal_confirm.UiKitConfirmModal_buttonContent.UiKitConfirmModal_textAlign')
        self.del_yes.click()
