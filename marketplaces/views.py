from django.shortcuts import render, redirect
from .models import Marketplace

def marketplaces(request):
    marketplace = Marketplace.objects.all()
    return render(request, 'marketplaces.html', {
        "marketplace":marketplace
    })



def catalog_redirect(request, slug):
    if slug == "uzum":
        return redirect("uzum:uzum_catalog")
    elif slug == "ozon":
        return redirect("ozon:ozon_catalog")
    else:
        return redirect("/")

