from django.shortcuts import render
from .models import Product

# Create your views here.
def index(request):
    return render(request, 'index.html')



def list_product(request):
    return render(request, 'products.html')



def product_details(request):
    product_list=Product.objects.all()
    context={
        'products': product_list
    }
    
    return render(request, 'product_details.html',context)









