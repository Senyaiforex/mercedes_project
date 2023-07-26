from django.core.management import BaseCommand
from coreapp.models import Product, Counter
import os


class Command(BaseCommand):
    """
    Applies all fixtures to the database
    """

    def handle(self, *args, **options):
        self.stdout.write("=" * 40 +
                          "\nApply all fixtures to the database\n\n")
        with open('coreapp/autonew.csv') as file:
            for line in file:
                list_product_requisites = line.split(';')
                price = list_product_requisites[-1]
                Product.objects.create(
                    article=list_product_requisites[0],
                    name=list_product_requisites[1],
                    price=price,
                )
            self.stdout.write(self.style.SUCCESS(
                "Fixtures applied successfully\n" + "=" * 40))
        Counter.objects.create(
            num_of_entries=0,
            name='entry'
        )
