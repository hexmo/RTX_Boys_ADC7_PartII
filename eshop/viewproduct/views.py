from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,context
from productmanagement.models import Product,Phones,Accessories,Laptop
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

# homepage
def homepage(request):
    product = Product.objects.all()
    params = {'products':product}
    return render(request,'viewproduct/home.html',params)

# displaying specific product
def viewProductDetails(request,ID):
    product = Product.objects.get(id=ID)
    # figuring out whether the product is phone, laptop, or accessory
    try:
        details = Phones.objects.get(product_id=ID)
        productType = 'phone'
    except Phones.DoesNotExist:
        details = Accessories.objects.get(product_id=ID)
        productType = 'accessories'
    except Accessories.DoesNotExist:
        details = Laptop.objects.get(product_id=ID)
        productType = 'laptop'

    context_varible = {'product':product, 'productType':productType, 'details':details}
    return render(request,'viewproduct/view.html',context_varible)


def viewPhones(request):
    # creating empty list
    product = []
    phones = Phones.objects.all()
    for phone in phones:
        product.append(Product.objects.get(id = phone.product_id))
    params = {'products':product}
    return render(request,'viewproduct/phones.html',params)

def viewLaptops(request):
    # creating empty list
    product = []
    laptops = Laptop.objects.all()
    for laptop in laptops:
        product.append(Product.objects.get(id = laptop.product_id))
    params = {'products':product}
    return render(request,'viewproduct/laptops.html',params)

def viewAccessories(request):
    # creating empty list
    product = []
    accessories = Accessories.objects.all()
    for accessory in accessories:
        product.append(Product.objects.get(id = accessory.product_id))
    params = {'products':product}
    return render(request,'viewproduct/accessories.html',params)
