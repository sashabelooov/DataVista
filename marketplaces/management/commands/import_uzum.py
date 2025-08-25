import csv
from django.core.management.base import BaseCommand
from ...models import Product, Marketplace


class Command(BaseCommand):
    help = "Import Uzum products from CSV file"

    def handle(self, *args, **kwargs):
        file_path = "Data/cleaned_uzummarket.csv"

        uzum_marketplace, _ = Marketplace.objects.get_or_create(
        slug="uzum",
        defaults={
            "name": "Uzum",
            "country": "Uzbekistan",
        }
    )

        # Eski ma’lumotlarni o‘chiramiz
        Product.objects.filter(marketplace=uzum_marketplace).delete()

        with open(file_path, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                title = row["Title"]
                price = row["Price"]
                rating = row["Rating"]
                comment = row["Comment"]
                color = row["Color"]

                Product.objects.create(
                    title=title,
                    marketplace=uzum_marketplace,
                    price=price,
                    rating=float(rating) if rating else None,
                    comment_number=int(float(comment)) if comment else 0,
                    color=color,
                )

        self.stdout.write(self.style.SUCCESS("✅ Uzum products imported successfully!"))
