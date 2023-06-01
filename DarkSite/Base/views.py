from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache
from .models import *

@never_cache
def my_view(request):
    products = Book.objects.all()[:10]
    return render(request, 'Base/index.html', {'products': products})

@login_required   
def cart_view(request):
    sum = 0
    if Cart.objects.filter(buyer = request.user):
        cart = Cart.objects.get(buyer = request.user)
    else:
        cart = Cart.objects.create(buyer = request.user)
        
    items = cart.items.all()
    for item in items:
        sum += item.total_price()
        
  
    return render(request,'Base/cart.html', {'cart':cart, 'sum':sum} )

@login_required
def add_cart(request, pk):
    book = Book.objects.get(id = pk)
    if Cart.objects.filter(buyer = request.user):
        cart = Cart.objects.get(buyer = request.user)
    else:
        cart = Cart.objects.create(buyer = request.user)
        
    cart_items = cart.items.all()
    for cart_item in cart_items:
        if cart_item.book.id == pk:
            cart_item.quantity = cart_item.quantity + 1
            cart_item.save()
            return render(request, 'Base/add_cart.html')

    cart_item = CartItem.objects.create(quantity =1 ,book = book) 
    cart.items.add(cart_item)
        
    return redirect('cart')

def detail_product(request, pk):
    product = Book.objects.get(id = pk)
    return render(request, 'Base/detail_product.html',{'product':product})

def filter_sach_khoa_hoc (request):
    category = Category.objects.get(name = "Sách khoa học")
    products = category.products.all()
    
    return render(request, 'Base/sach_khoa_hoc.html',{'products':products})

def filter_sach_lam_giau (request):
    category = Category.objects.get(name = "Sách làm giàu")
    products = category.products.all()
    
    return render(request, 'Base/sach_lam_giau.html',{'products':products})

def filter_sach_thieu_nhi (request):
    category = Category.objects.get(name = "Sách thiếu nhi")
    products = category.products.all()
    
    return render(request, 'Base/sach_thieu_nhi.html',{'products':products})





def search_feature(request):
    if request.method == 'POST':
        search_query = request.POST['productt']
        print(search_query)
        products = Book.objects.filter(title__icontains=search_query)
        return render(request, 'Base/search.html', {'query':search_query, 'products':products})
    else:
        return render(request, 'Base/search.html',{})
    
def delete_cart_item(request , pk):
    cart = Cart.objects.get(buyer = request.user)
    cart_item = CartItem.objects.get(id = pk)
    cart.items.remove(cart_item)
    
    return redirect('cart')
    



    
    


