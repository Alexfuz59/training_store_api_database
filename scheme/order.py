import re
from pydantic import BaseModel, field_validator
from enums.order_enums import Status


class Order(BaseModel):
    id: int
    payment_key: str
    status: Status
    total_price: int

    @field_validator('payment_key')
    def check_payment_key(cls, payment_key):
        pattern = r'cs_test_[\d\w]+'
        payment_key_result = re.fullmatch(pattern, payment_key)
        if not payment_key_result:
            raise ValueError('Invalid payment_key')
