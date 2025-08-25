from django.urls import path
from . import views

app_name = "ozon"

urlpatterns = [
    path("catalog/", views.ozon_catalog, name="ozon_catalog"),
]
