from django.shortcuts import render,get_object_or_404,redirect
from django.views import View
from product.models import Product,Cart
from decimal import Decimal
from django.contrib import messages

# Create your views here.


def Home(request):
    products = Product.objects.all() 
    context = { 'products': products, }
    return render(request, 'Homepage.html',context)

class ProductDetail(View):
    def get(self,request,pk):
        product = get_object_or_404(Product, pk=pk)
        return render (request,'Outerweardetail.html',{'product':product})

# def OuterWear(request):
#     products = Product.objects.filter(category="OW")
#     brand = request.GET.get('brand')
#     if brand and brand != 'All':
#             products = products.filter(brand=brand)
#     context = { 'products': products, }
#     return render (request,"Outerwear.html",context)


# def OuterWear(request):
#     # Get all products in the "Outerwear" category
#     products = Product.objects.filter(category="OW")
    
#     # Fetch unique brand names dynamically from the database
#     brands = Product.objects.filter(category="OW").values_list('brand', flat=True).distinct()
    
#     # Get the brand filter from the GET request (if any)
#     brand = request.GET.get('brand')
    
#     # Apply filtering if a specific brand is selected and it's not 'All'
#     if brand and brand != 'All':
#         products = products.filter(brand=brand)
    
#     # Pass products and brand list to the template
#     context = {
#         'products': products,
#         'brands': brands,
#         'selected_brand': brand,  # To highlight the selected brand in the template
#     }
    
#     return render(request, "Outerwear.html", context)



def OuterWear(request):
    # Get all products in the "Outerwear" category
    products = Product.objects.filter(category="OW")
    
    # Fetch unique brand names dynamically from the database
    brands = Product.objects.filter(category="OW").values_list('brand', flat=True).distinct()
    
    # Get the brand filter from the GET request (if any)
    brand = request.GET.get('brand')
    if brand and brand != 'All':
        products = products.filter(brand=brand)
    
    # Get the sort filter from the GET request (if any)
    sort_by = request.GET.get('sort_by')
    if sort_by == 'low_to_high':
        products = products.order_by('selling_price')
    elif sort_by == 'high_to_low':
        products = products.order_by('-selling_price')
    
    # Pass products, brand list, and sorting to the template
    context = {
        'products': products,
        'brands': brands,
        'selected_brand': brand,  # To highlight the selected brand in the template
        'selected_sort': sort_by,  # To maintain the selected sort order in the dropdown
    }
    
    return render(request, "Outerwear.html", context)


# def AddCart(request):
#     user= request.user
#     product_id = request.GET.get('prod_id')
#     product = Product.objects.get(id=product_id)
#     Cart(user=user, product=product).save()
#     return redirect('Show_Cart')



def AddCart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
        
    # Check if the product is already in the cart
    cart_item = Cart.objects.filter(user=user, product=product).first()
    if cart_item:
        messages.info(request, 'Selected product is already in cart')
    else:
        Cart(user=user, product=product).save()
        
    return redirect('Show_Cart')






def ShowCart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = Decimal(0.0)  # Use Decimal for consistency
        shipping_amount = Decimal(70.0)  # Convert shipping amount to Decimal
        total_amount = Decimal(0.0)
        cart_product = Cart.objects.filter(user=user)  # Filter by user directly in the query
        
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity * p.product.discounted_price)  # Assume discounted_price is Decimal
                amount += tempamount
            total_amount = amount + shipping_amount
        
        return render(request, 'cart.html', {'carts': cart, 'total_amount': total_amount, 'amount': amount})
    else:
        return redirect('login')  # Redirect to login if the user is not authenticated
       
