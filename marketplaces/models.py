from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Marketplace(models.Model):
    name = models.CharField(max_length=100)  
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

    image = models.ImageField(upload_to="marketplaces/")  
    created_at = models.DateField(auto_now_add=True)  

    def __str__(self):
        return self.name
