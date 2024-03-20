from pydantic import BaseModel
from scheme.order import Order
from typing import List


class ListOrders(BaseModel):
    data: List[Order]


