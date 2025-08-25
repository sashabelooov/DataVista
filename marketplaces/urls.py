from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.marketplaces, name='marketplaces'),
    path('uzum/', include('uzum.urls')),
    path('ozon/', include('ozon.urls')),
    path('catalog/<slug:slug>/', views.catalog_redirect, name='catalog_redirect'),
]