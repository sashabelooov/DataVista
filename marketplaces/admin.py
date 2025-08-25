from django.contrib import admin
from .models import Marketplace, Product



@admin.register(Marketplace)
class MarketplaceAdmin(admin.ModelAdmin):
    list_display = ("name", "country", "created_at")
    search_fields = ("name", "country")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('marketplace','title', 'price', 'rating', 'comment_number', 'color')
    list_filter = ('title', 'price', 'color')
    search_fields = ('title', )