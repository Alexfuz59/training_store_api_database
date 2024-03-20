import requests
import allure
from base.base_api import BaseAPI
from config.link import Link
from builder.payload import UpdateOrderDate


class UpdateOrder(BaseAPI):

    def __init__(self):
        super().__init__()
        self.url = Link()
        self.payload = UpdateOrderDate()

    @allure.step('Update status order')
    def update_order(self, order):
        self.response = requests.put(
            url=self.url.UPDATE_ORDER,
            json=self.payload.update_data(order)
        )
        self.response_json = self.response.json()
        self.attach_response()
