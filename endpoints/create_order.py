import requests
import allure
from base.base_api import BaseAPI
from config.link import Link
from builder.payload import CreateOrderDate
from scheme.order import Order


class CreateOrder(BaseAPI):
    SCHEMA = Order

    def __init__(self):
        super().__init__()
        self.url = Link()
        self.payload = CreateOrderDate()

    @allure.step('Create order')
    def create_order(self):
        self.response = requests.post(
            url=self.url.CREATE_ORDER,
            json=self.payload.order_data()
        )
        self.response_json = self.response.json()
        self.attach_response()
