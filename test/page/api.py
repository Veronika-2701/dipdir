import requests
import allure


@allure.epic("Деливери")
@allure.severity("blocker")
class Delivery:
    """Этот класс представляет сущность сайта Деливери."""
    @allure.id("инициализация сайта Деливери")
    def __init__(self, base_url) -> None:
        """Эта функция инициализирует base_url и токен"""
        self.base_url = base_url
        self.token = 'y0__xC-o82NCBix9BwgoqaE9xJ1Tcj7XI9x9eHMBceDtzWvNhnNgA'

    @allure.id("Request Get-запроса")
    def req_get(self, req_type="GET", url="", data={}):
        """Эта функция создает оболочку Request Get-запроса"""
        headers = {
            'Authorization': 'Bearer ' + self.token,
            'Accept': 'application/json'
            }
        return requests.request(req_type,
                                self.base_url + url,
                                headers=headers,
                                json=data)

    @allure.id("Request Post-запроса")
    def req_post(self, req_type="POST", url="", data={}):
        """Эта функция создает оболочку Request Post-запроса"""
        headers = {
            'Authorization': 'Bearer ' + self.token,
            'Accept': 'application/json,'
            'text/plain, */*'
            }
        return requests.request(req_type,
                                self.base_url + url,
                                headers=headers,
                                json=data)

    @allure.id("Request Put-запроса")
    def req_put(self, req_type="PUT", url="", data={}):
        """Эта функция создает оболочку Request Put-запроса"""
        headers = {
            'Authorization': 'Bearer ' + self.token,
            'Accept': 'application/json'
            }
        return requests.request(req_type,
                                self.base_url + url,
                                headers=headers,
                                json=data)
