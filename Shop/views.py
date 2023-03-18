from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json
import datetime

def home(request):
    return render(request, 'Shop/home.html')


def user(request):
    return render(request, 'Shop/user.html')


def register(request):
    return render(request, 'Shop/register.html')

def login(request):
    return render(request, 'Shop/login.html')

def about(request):
    return render(request, 'Shop/about.html')


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()  # get all orderitems of particular order
    else:
        items = []
    context = {'items':items, 'order':order}
    return render(request, 'Shop/cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()  # get all orderitems of particular order
    else:
        items = []
    context = {'items':items, 'order':order}
    return render(request, 'Shop/checkout.html', context)


def dark(request):
    sabers = Saber.objects.filter(category='DS')
    context = {'sabers':sabers}
    return render(request, 'Shop/dark.html', context)


def light(request):
    sabers = Saber.objects.filter(category='LS')
    context = {'sabers': sabers}
    return render(request, 'Shop/light.html', context)


def updateItem(request):
    data = json.loads(request.body)
    saberId = data['saberId']
    action = data['action']

    print('Action: ', action)
    print('saberId', saberId)

    customer = request.user.customer
    saber = Saber.objects.get(id=saberId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, saber=saber)

    if action == 'add':
        orderItem.save()
        return JsonResponse('item added', safe=False)
    elif action == 'remove':
        orderItem.delete()
        return JsonResponse('item removed', safe=False)
    return JsonResponse('?', safe=False)


def placeOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    order.transaction_id = transaction_id

    ShippingInfo.objects.create(
        customer=customer,
        order=order,
        country=data['shippingInfo']['country'],
        city=data['shippingInfo']['city'],
        address=data['shippingInfo']['address'],
        zip=data['shippingInfo']['zip']
    )
    print('Data:', request.body)
    return JsonResponse('Order placed', safe=False)
