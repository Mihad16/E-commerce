from django.shortcuts import render
from .models import Product

# Create your views here.
def index(request):
    return render(request, 'index.html')



def list_product(request):
    product_list=Product.objects.all()
    context={
        'products': product_list
    }
    return render(request, 'products.html', context)




def product_details(request):
    product_list=Product.objects.all()
    context={
        'products': product_list
    }
    
    return render(request, 'product_details.html',context)









