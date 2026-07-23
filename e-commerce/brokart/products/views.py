from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    return render(request, 'index.html')



def list_product(request):
    page=1
    if request.method=='GET':
        page=request.GET.get('page',1)
    product_list=Product.objects.all()
    products_paginator = Paginator(product_list, 3)  # Show 4 products per page
    products_page_number = products_paginator.get_page(page)

    return render(request, 'products.html', {'products': products_page_number})




def product_details(request, pk):
    product=Product.objects.get(pk=pk)
    product_list=Product.objects.all()
    context={'products':product,'product_list':product_list}
    
    return render(request, 'product_details.html',context)









