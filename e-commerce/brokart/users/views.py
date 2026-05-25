from django.shortcuts import render

# Create your views here.
def show_account(request):
    return render(request, 'account.html')

def cart(request):
    return render(request, 'cart.html')

def contact(request):
    return render(request, 'contact.html')
