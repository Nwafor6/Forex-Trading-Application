from django.core.management.base import BaseCommand
from mainapp.task2 import start_data_fetching_thread


class Command(BaseCommand):
    help = 'Start data fetching thread'

    def handle(self, *args, **options):
        start_data_fetching_thread()
