from django.urls import path
from . import views

app_name = "uzum"

urlpatterns = [
    path("catalog/", views.uzum_catalog, name="uzum_catalog"),
    path('product_list/', views.product_list, name='product_list'),

]
