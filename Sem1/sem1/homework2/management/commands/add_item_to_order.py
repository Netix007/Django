from django.core.management.base import BaseCommand
from homework2.models import Item, Order


class Command(BaseCommand):
    help = 'Add item to order'

    def add_arguments(self, parser):
        parser.add_argument('item_id', type=int, help='Item ID.')
        parser.add_argument('order_id', type=int, help='Order ID.')

    def handle(self, *args, **options):
        item_id = options.get('item_id')
        order_id = options.get('order_id')
        order = Order.objects.filter(pk=order_id).first()
        item = Item.objects.filter(pk=item_id).first()
        order.products.add(item)
        order.total_price += item.price
        order.save()
        self.stdout.write(f'Item {item_id} was added to order {order_id}')
