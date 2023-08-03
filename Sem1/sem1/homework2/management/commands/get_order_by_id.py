from django.core.management.base import BaseCommand
from homework2.models import Order


class Command(BaseCommand):
    help = "Find order by ID"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Order ID.')

    def handle(self, *args, **options):
        pk = options.get('pk')
        order = Order.objects.filter(pk=pk).first()
        self.stdout.write(f'Order ID: {order.id} Customer: {order.customer.name} \n'
                          f'Email: {order.customer.email} Phone: {order.customer.phone_number} \n')
        self.stdout.write(f'{order.products.all()} \n Total cost: {order.total_price}')
