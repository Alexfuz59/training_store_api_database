import pytest
from endpoints.create_order import CreateOrder
from endpoints.get_order import GetOrders
from endpoints.update_order import UpdateOrder
from endpoints.delete_order import DeleteOrders
from database.database_orders import Database


class BaseTest:
    create_order: CreateOrder
    get_order: GetOrders
    update_order: UpdateOrder
    delete_order: DeleteOrders
    database_orders: Database

    @pytest.fixture(autouse=True, scope='function')
    def setup(self, request, cursor):
        request.cls.cursor = cursor
        request.cls.create_order = CreateOrder()
        request.cls.get_order = GetOrders()
        request.cls.update_order = UpdateOrder()
        request.cls.delete_order = DeleteOrders()
        request.cls.database_orders = Database(cursor)
