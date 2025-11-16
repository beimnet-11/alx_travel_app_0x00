from django.core.management.base import BaseCommand
from listings.models import Listing
from faker import Faker
import random

fake = Faker()


class Command(BaseCommand):
    help = "Seed the database with sample listings"

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS("Starting database seeding..."))

        for _ in range(10):
            Listing.objects.create(
                title=fake.sentence(nb_words=4),
                description=fake.paragraph(nb_sentences=3),
                price_per_night=random.randint(30, 500),
                location=fake.city(),
            )

        self.stdout.write(self.style.SUCCESS("Database seeding completed successfully!"))
