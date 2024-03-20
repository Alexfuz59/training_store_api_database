import allure
from scheme.order import Order


class Database:
    SCHEMA = Order
    responseDB = None

    def __init__(self, cursor):
        self.cursor = cursor

    @allure.step('Get last order from database')
    def last_order(self):
        self.cursor.execute('SELECT * FROM orders ORDER BY id DESC LIMIT 1')
        data = self.cursor.fetchall()
        headers = ['id', 'total_price', 'status', 'payment_key' ]
        for row in data:
            self.responseDB = (dict(zip(headers, row)))

    @allure.step('Checking number of orders in the database')
    def check_len_orders(self, orders_api):
        self.cursor.execute('SELECT COUNT(id) FROM orders')
        len_database = self.cursor.fetchall()[0][0]
        assert len(orders_api) == len_database, "Incorrect number of orders in database"

    @allure.step('Validation of order attributes in database')
    def validate_schema_database(self):
        parsed_object = self.SCHEMA.model_validate(self.responseDB)
        return parsed_object

    @allure.step('Check order in the database')
    def check_order(self, order_api, oder_database):
        assert order_api.id == oder_database.id, "Invalid ID in database"
        assert order_api.status == oder_database.status, "Invalid STATUS in database"
        assert order_api.payment_key == oder_database.payment_key, "Invalid PAYMENT_KEY in database"
        assert order_api.total_price == oder_database.total_price, "Invalid TOTAL_PRICE in database"

    @allure.step('Checking order deletion in the database')
    def check_delete_order(self, order):
        self.cursor.execute(f'SELECT COUNT(*) FROM orders WHERE id={order.id}')
        number_order_id = (self.cursor.fetchall())[0][0]
        assert number_order_id == 0, "The order has not been deleted from the database"

    @allure.step('Check order status in the database')
    def check_status_order(self, order):
        self.cursor.execute(f'SELECT * FROM orders WHERE id={order.id}')
        order = self.cursor.fetchall()
        headers = ['id', 'total_price', 'status', 'payment_key']
        for row in order:
            self.responseDB = (dict(zip(headers, row)))
        assert self.responseDB['status'] == "paid", "Order status has not changed"
