from django.core.management.base import BaseCommand
from vacancy.models import VacancyCategory

from django.utils.text import slugify

class Command(BaseCommand):
    help = "Create 20 predefined vacancy categories"

    CATEGORIES = [
        "UPSC", "SSC", "Banking", "Railway", "Defence", "Paramilitary",
        "Police", "Teaching", "Medical", "Nursing", "Engineering",
        "IT / Technical", "PSU", "Insurance", "Judiciary", "Agriculture",
        "Research", "State Government", "Municipal", "Others"
    ]

    def handle(self, *args, **kwargs):
        for name in self.CATEGORIES:
            VacancyCategory.objects.update_or_create(
                name=name,
                defaults={"slug": slugify(name)}
            )
        self.stdout.write(self.style.SUCCESS("20 categories created!"))
