from django.core.management.base import BaseCommand
from sem2_task1.models import CoinPlay
from random import randint


class Command(BaseCommand):
    help = 'Throw a coin.'

    def handle(self, *args, **options):
        CoinPlay.add_throws(randint(0, 1))
