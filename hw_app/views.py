from django.http import HttpResponse
from random import randint
from .models import *
from random import *


# ----------- Вывод на экран ----------------------
def text(title, result=None, list_data=None):
    result_string = f'<h1>{title}</h1>' \
                    f'<h3>{result}</h3>'
    if list_data is not None:
        for el in list_data:
            result_string += f'<p>{el}</p>'
    return result_string


# ------- Главная страница ------------------------
def general(request):
    title = 'Стартовая страница'
    result = 'Сервер запущен'
    return HttpResponse(text(title, result))


# ------- Тестовые ползователи ----------------------
def create_fake_users(request):
    title = 'Тестовые пользователи'
    result = 'Список пользователей создан'
    for i in range(1, 6):
        user = User(
            name=f'Name_{i}',
            email=f'e{i}@mail.com',
            mobile=f'+7 (999) 555-44-0{i}',
            us_adrs=f'Регион, Город, Улица, Дом, Кв.',
        )
        user.save()
    return HttpResponse(text(title, result))


def list_fake_users(request):
    title = 'Список пользователей'
    result = 'Общий список загружен'
    users = []
    for user in User.objects.all():
        users.append(user.full_data())
    return HttpResponse(text(title, result, users))


# ------- Тестовые товары ------------------------
def create_fake_products(request):
    title = 'Тестовые Товары'
    result = 'Список тестовых товаров создан'
    for i in range(1, 21):
        prdt = Product(
            name=f'Товар - {i}',
            content=f'Описание товара ...',
            price=uniform(500, 10000),
            count=randint(1,20),
        )
        prdt.save()
    return HttpResponse(text(title, result))


def list_fake_products(request):
    title = 'Список товаров'
    result = 'Общий список товаров загружен'
    prts = []
    for prdt in Product.objects.all():
        prts.append(prdt.full_data())
    return HttpResponse(text(title, result, prts))


# ------- Тестовые заказы ------------------------
def create_fake_orders(request):
    title = 'Тестовые заказы'
    result = 'Список тестовых заказов создан'
    for user in User.objects.all():
        order = Order(us_name=user)
        order.save()
        sum_price = 0
        for _ in range(5):
            pid = randint(1, 20)
            prd = Product.objects.filter(pk=pid).first()
            order.products.add(prd)
            sum_price += prd.price_get()
        order.sum_price = sum_price
        order.save()
    return HttpResponse(text(title, result))


def list_fake_orders(request):
    title = 'Список заказов'
    result = 'Общий список заказов загружен'
    orders = []
    for order in Order.objects.all():
        orders.append(order)
        print(order.products)
    return HttpResponse(text(title, result, orders))