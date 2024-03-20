import requests
import allure
from base.base_api import BaseAPI
from config.link import Link


class DeleteOrders(BaseAPI):

    def __init__(self):
        super().__init__()
        self.url = Link()

    @allure.step('Delete order')
    def delete_orders(self, order):
        self.response = requests.delete(
            url=self.url.DELETE_ORDER(order.id)
        )
