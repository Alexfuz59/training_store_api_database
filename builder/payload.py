from faker import Faker
from random import randint

fake = Faker()


class CreateOrderDate:
    @staticmethod
    def order_data():
        name = fake.first_name()
        image = fake.image_url()
        price = randint(1, 100)
        quantity = randint(1, 10)
        return {
            'products': [
                {'name': name,
                 'image': image,
                 'price': price,
                 'quantity': quantity
                 }
            ]
        }


class UpdateOrderDate:

    @staticmethod
    def update_data(order):
        status = "paid"
        id = order.id
        total_price = order.total_price,
        payment_key = order.payment_key
        return {
            'id': id,
            'status': status,
            'total_price': total_price,
            'payment_key': payment_key
        }
