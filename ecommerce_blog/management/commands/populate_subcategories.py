from typing import Any
from ecommerce_blog.models import Subcategory, Category
from django.core.management.base import BaseCommand

# import random

class Command(BaseCommand):
    help = "This commands insert Subcategory data "

    def handle(self, *args, **options):
        # return super().handle(*args, **options)
        # delete existing data
        Subcategory.objects.all().delete()

        # subcategories = ['carrot','nut','grapes','almond','dates']

        subcategories = Category.objects.all()

        for subcategory_name in subcategories:
            # subcategory = random.choice(subcategories)
            Subcategory.objects.create(subname = subcategory_name)
        
        self.stdout.write(self.style.SUCCESS("sub categories Compleated insearting Data!"))