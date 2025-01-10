from typing import Any
from ecommerce_blog.models import Category
from django.core.management.base import BaseCommand



class Command(BaseCommand):
    help = "This commands insert post data "

    def handle(self, *args, **options):
        # return super().handle(*args, **options)
        # delete existing data
        # Category.objects.all().delete()

        categories = ['vegetables','groceries','fruits','dairy farms','diet foods']

        # categories = Category.objects.all()

        for category_name in categories:
            Category.objects.create(name = category_name)
        
        self.stdout.write(self.style.SUCCESS("category Compleated insearting Data!"))