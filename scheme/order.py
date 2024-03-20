from pydantic import BaseModel
from enums.order_enums import Status


class Order(BaseModel):
    id: int
    payment_key: str
    status: Status
    total_price: int
