BASE_URL = "http://16.170.215.221:9090/api/v1"


class Link:
    GET_ORDERS = f'{BASE_URL}/orders'
    CREATE_ORDER = f'{BASE_URL}/orders'
    UPDATE_ORDER = f'{BASE_URL}/orders'
    DELETE_ORDER = lambda self, order_id: f'{BASE_URL}/orders/{order_id}'
