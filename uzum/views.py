from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from marketplaces.models import Marketplace, Product

def uzum_catalog(request):
    return render(request, 'uzum_catalog.html')




def product_list(request):
    # Faqat UzumMarket mahsulotlari
    marketplace = get_object_or_404(Marketplace, name="UzumMarket")
    products = Product.objects.filter(marketplace=marketplace).order_by("-id")

    return render(request, "products_list.html", {
        "marketplace": marketplace,
        "products": products,
    })

