from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Marketplace(models.Model):
    name = models.CharField(max_length=100, unique=True)  
    country = models.CharField(max_length=50)  
    slug = models.SlugField(unique=True)
    rating = models.DecimalField(
        max_digits=2, 
        decimal_places=1, 
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)], 
        null=True, 
        blank=True
    )

    number_of_reviews = models.BigIntegerField(null=True, blank=True)  
    number_of_products = models.BigIntegerField(null=True, blank=True)  

    image = models.ImageField(
    upload_to="marketplaces/",
    blank=True,
    null=True,
    )

    created_at = models.DateField(auto_now_add=True)  

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=255)
    marketplace = models.ForeignKey(Marketplace, on_delete=models.CASCADE, null=False, blank=False)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    rating = models.DecimalField(
        max_digits=2, 
        decimal_places=1, 
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)], 
        null=True, 
        blank=True
    )
    comment_number = models.IntegerField(default=0)
    color = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(
        upload_to="products/",
        blank=True,
        null=True,
        default="products/i.webp"  # default rasm
    )

    def __str__(self):
        return self.title









