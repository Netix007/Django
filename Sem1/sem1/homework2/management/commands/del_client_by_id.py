from django.core.management.base import BaseCommand
from homework2.models import Client


class Command(BaseCommand):
    help = "Delete client by ID"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID.')

    def handle(self, *args, **options):
        pk = options.get('pk')
        client = Client.objects.filter(pk=pk).first()
        client.delete()
        self.stdout.write(f'Client with id {pk} was deleted.')
