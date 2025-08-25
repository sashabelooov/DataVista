from django.shortcuts import render

def ozon_catalog(request):
    return render(request, 'ozon_catalogs.html')