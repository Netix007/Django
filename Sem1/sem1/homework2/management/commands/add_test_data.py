from django.core.management.base import BaseCommand
from homework2.models import Client, Item, Order
from random import randint


class Command(BaseCommand):
    help = 'Add fake clients, items and orders'

    def add_arguments(self, parser):
        parser.add_argument('amount_clients', type=int, help='Amount of fake clients.')
        parser.add_argument('amount_items', type=int, help='Amount of fake items.')
        parser.add_argument('amount_orders', type=int, help='Amount of fake orders.')

    def handle(self, *args, **options):
        amount_clients = options.get('amount_clients')
        amount_items = options.get('amount_items')
        amount_orders = options.get('amount_orders')
        for i in range(1, amount_clients + 1):
            client = Client(
                name=f'Client {i}',
                email=f'mail{i:0>4}@mail.com',
                phone_number="+" + "".join([str(randint(0, 9)) for _ in range(0, randint(9, 15))]),
                address=f'Address client {i}',
            )
            client.save()
            self.stdout.write(f'{client}')
        for i in range(1, amount_items + 1):
            item = Item(
                name=f'Item {i}',
                description=f'Lorem description for item {i}',
                price=randint(1, 100),
                count=randint(1, 100),
            )
            item.save()
            self.stdout.write(f'{item}')
        for i in range(1, amount_orders + 1):
            add_client = Client.objects.order_by("?").first()
            add_item = Item.objects.order_by("?").first()
            order = Order(
                customer=add_client,

                total_price=add_item.price,
            )
            order.save()
            Order.objects.latest('id').products.add(add_item)
            view_order = Order.objects.latest('id')
            self.stdout.write(f'{view_order}')
