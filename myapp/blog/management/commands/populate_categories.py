from blog.models import Category
from django.core.management.base import BaseCommand
from typing import Any

class Command(BaseCommand):
    help="this command insert categories data"
    
    def handle(self, *args:Any, **options:Any):
        #delete exitsing data
        Category.objects.all().delete()

        categories=[
                        "software Development",
                        "Artificial Intelligence",
                        "Web Development",
                        "Cybersecurity ",
                        "Debugging ",
                        "Database Development",
                        "Tech Culture ",
                        "Concurrency "
                    ]
        

        for category_name in categories:
            Category.objects.create(name=category_name)

        self.stdout.write(self.style.SUCCESS("completed inserting data!"))
