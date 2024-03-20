import pytest
import allure
from base.base_test import BaseTest


@allure.feature('Orders')
class TestOrders(BaseTest):
    @pytest.fixture()
    def order(self):
        self.create_order.create_order()
        self.create_order.check_response_is_200()
        order = self.create_order.validate_scheme()
        yield order
        self.delete_order.delete_orders(order)

    @allure.title('Create order')
    def test_create_order(self):
        self.create_order.create_order()
        self.create_order.check_response_is_200()
        order_api = self.create_order.validate_scheme()
        self.database_orders.last_order()
        order_database = self.database_orders.validate_schema_database()
        self.database_orders.check_order(order_api, order_database)

    @allure.title('List all orders')
    def test_get_orders(self):
        self.get_order.get_orders()
        self.get_order.check_response_is_200()
        orders_api = self.get_order.validate_scheme_orders()
        self.database_orders.check_len_orders(orders_api)

    @allure.title('Update status order')
    def test_update_order(self, order):
        self.update_order.update_order(order)
        self.update_order.check_response_is_200()
        self.update_order.validate_scheme()
        self.database_orders.check_status_order(order)

    @allure.title('Delete order')
    def test_delete_order(self, order):
        self.delete_order.delete_orders(order)
        self.delete_order.check_response_is_200()
        self.database_orders.check_delete_order(order)





