from django.shortcuts import render
from store.models import *
from django.http import JsonResponse
import json

# Create your views here.
def main(request):
    context = {}
    return render(request, 'store/main.html', context)

def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete= False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_item
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_item':0}
        cartItems = order['get_cart_items']

    products = Product.objects.all()
    context = {'products': products, 'cartItems': cartItems, 'shipping': False}
    return render(request, 'store/store.html', context)

def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete= False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_item
    else:
        # try:
        #     cart = json.load(request.COOKIES['cart'])
        # except:
        #     cart = {}

        items = []
        order = {'get_cart_total':0, 'get_cart_item':0, 'shipping': False}
        cartItems = order['get_cart_items']

        # for i in cart:
        #     cartitems += cart[i]['quantity']
        #     product = product.object.get(id = i)
        #     total = (product.price * cart[i]['quantity'])

        #     order['get_cart_total'] += total
        #     order['get_cart_item'] += cart[i]['quantity']

        #     item = {
        #         'product':{
        #             'id': product.id,
        #             'name': product.name,
        #             'price': product.price,
        #             'imageURL': product.imageURL,
        #         },
        #         'quality': cart[i]['quantity'],
        #         'get_total': total
        #     }
        #     items.append(item)

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete= False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_item
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_item':0, 'shipping': False}
        cartItems = order['get_cart_items']
    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/checkout.html', context)


def updateItem(request):
    data = json.loads(request.body.decode("utf-8"))
    productId = data['productId']
    action = data['action']
    # print('Product:', productId) 
    # print('Action:', action) 

    customer = request.user.customer
    product = Product.objects.get(id = productId)
    order, created = Order.objects.get_or_create(customer=customer, complete= False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = orderItem.quantity + 1
    elif action == 'remove':
        orderItem.quantity = orderItem.quantity - 1

    orderItem.save()

    if orderItem.quantity <=0:
        orderItem.delete()
    return JsonResponse('Item was added', safe=False) 


def processOrder(request):
    print('Data:', request.body)
    return JsonResponse('payment submittem', safe = False)