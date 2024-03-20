import requests
import allure
from base.base_api import BaseAPI
from config.link import Link
from scheme.order import Order


class GetOrders(BaseAPI):
    SCHEMA = Order

    def __init__(self):
        super().__init__()
        self.url = Link()

    @allure.step('List orders')
    def get_orders(self):
        self.response = requests.get(
            url=self.url.GET_ORDERS
        )
        self.response_json = self.response.json()
        self.attach_response()

    @allure.step('Validate list orders')
    def validate_scheme_orders(self):
        parsed_object = [self.SCHEMA(**item) for item in self.response.json()]
        return parsed_object
