from django.shortcuts import render, get_object_or_404, redirect
from .forms import *
from random import *
from datetime import datetime, date


# ------- Главная страница --------------------------------
def general(request):
    context = {
        "title": 'Главная',
        "head": 'Стартовая страница',
        "text": 'Сервер запущен и работает',
    }
    return render(request, "hw_app/general.html", context)


# ------- Завершающая страница ----------------------------
def complete(request):
    context = {
        "title": 'Изменения',
        "head": 'Изменения',
        "text": 'Изменения вступили в силу',
    }
    return render(request, "hw_app/complete.html", context)


# ------- Тестовые данные ---------------------------------
def fake_datas(request, urs, pds, ods):
    if urs:
        for i in range(5):
            user = User(
                name=f'Пользователь {i}',
                email=f'e{i}@mail.com',
                mobile=f'+7 (999) 555-44-0{i}',
                us_adrs=f'Регион, Город, Улица, Дом, Кв.',
                reg_day=date.today()
            )
            user.save()
    if pds:
        for i in range(1, 8):
            product = Product(
                name=f'Товар - {i}',
                content=f'Описание товара ...',
                price=uniform(500, 10000),
                count=randint(1, 20),
                add_day=date.today(),
                image=None
            )
            product.save()
    if ods:
        for user in User.objects.all():
            order = Order(us_name=user, order_day=date.today())
            order.save()
            sum_price = 0
            l_pid = sample(list(i for i in range(1, len(Product.objects.all())+1)), 5)
            for pid in l_pid:
                order_product = Product.objects.filter(pk=pid).first()
                sum_price += order_product.price_get()
                order.products.add(order_product)
            order.sum_price = sum_price
            order.save()
    context = {
        "title": 'Data',
        "head": 'Fakes data',
        "text": 'Create fakes data is complete',
    }
    return render(request, "hw_app/general.html", context)


# ------- Список клентов ----------------------------------
def list_users(request):
    context = {
        "title": 'Список клиентов',
        "head": 'Список клиентов',
        "text": 'Список заргружен корректно',
        "users": User.objects.all()
    }
    return render(request, "hw_app/dbu.html", context)


# ------- Список товаров ----------------------------------
def list_products(request):
    context = {
        "title": 'Список товаров',
        "head": 'Список товаров',
        "text": 'Список заргружен корректно',
        "products": Product.objects.all(),
    }
    return render(request, "hw_app/dbp.html", context)


# ------- Список заказов ----------------------------------
def list_orders(request):
    context = {
        "title": 'Список заказов',
        "head": 'Список заказов',
        "text": 'Список заргружен корректно',
        "orders": Order.objects.all(),
    }
    return render(request, "hw_app/dbo.html", context)


# ------- Список товаров в заказе -------------------------
def basket(request, oid):
    context = {
        "title": 'Список товаров заказа',
        "text": 'Список заргружен корректно',
        'head': Order.objects.get(pk=oid).us_name,
        'basket': Order.objects.get(pk=oid).products.all(),
    }
    return render(request, "hw_app/dbbasket.html", context)


# ------- Список товаров клиента --------------------------
def us_products(request, uid):
    user = get_object_or_404(User, pk=uid)
    orders_list = Order.objects.filter(us_name=user)
    products_list = []
    for el in orders_list:
        products_list += Order.objects.get(pk=el.id).products.all()
    context = {
        "title": 'Список клиента',
        "head": 'Список товаров клиента',
        "text": 'Список заргружен корректно',
        'user_products': products_list,
    }
    return render(request, 'hw_app/us_prod.html', context)


# ------- Список товаров с отсевом по времени -------------
def us_products_time(request, uid, dif_day):
    user = get_object_or_404(User, pk=uid)
    orders_list = Order.objects.filter(us_name=user)
    products_list = []
    for el in orders_list:
        delta = abs(el.order_day.replace(tzinfo=None) - datetime.utcnow())
        if delta.days < dif_day:
            products_list += Order.objects.get(pk=el.id).products.all()
    products_list = list(set(products_list))
    products_list.sort(key=lambda x: x.add_day)
    context = {
        "title": 'Фил-ый список',
        "head": 'Отфильтрованный список продуктов',
        "text": 'Список заргружен корректно',
        'user_products': products_list,
    }
    return render(request, 'hw_app/us_prod.html', context)


# ------------------------ ФОРМЫ --------------------------
# --------------------- Список форм -----------------------
def adds(request):
    context = {
        "title": 'Список форм',
        "head": 'Список форм',
    }
    return render(request, 'hw_app/list_data.html', context)


# ----------------- Создание клиента --------------
def add_user(request):
    if request.method == 'POST':
        us_form(request)
        return redirect('complete')
    else:
        form = UserForm()
        context = {
            "title": 'Форма клиента',
            "head": 'Форма для заполнения клиента',
            'form': form,
            'button': 'Создать клиента'
        }
        return render(request, 'hw_app/form.html', context)


# ----------------- Изменение клиента --------------
def ch_user(request, uid):
    if request.method == 'POST':
        us_form(request, uid)
        return redirect('complete')
    else:
        form = UserForm()
        context = {
            "title": 'Форма клиента',
            "head": 'Форма для заполнения клиента',
            'form': form,
            'button': 'Изменить клиента'
        }
        return render(request, 'hw_app/form.html', context)


# ----------------- Создание товара --------------
def add_product(request):
    if request.method == 'POST' and request.FILES:
        prdt_form(request)
        return redirect('complete')
    else:
        form = ProductForm()
        context = {
            "title": 'Форма товара',
            "head": 'Форма для заполнения товара',
            "button": 'Создать товар',
            'form': form,
        }
        return render(request, 'hw_app/form.html', context)


# ----------------- Изменение товара --------------
def ch_product(request, pid):
    if request.method == 'POST' and request.FILES:
        prdt_form(request, pid)
        return redirect('complete')
    else:
        form = ProductForm()
        context = {
            "title": 'Форма товара',
            "head": 'Форма для заполнения товара',
            'form': form,
            'button': 'Изменить товар'
        }
        return render(request, 'hw_app/form.html', context)


# ----------------- Универсальная форма клиента --------------
def us_form(request, uid=None):
    form = UserForm(request.POST)
    if form.is_valid():
        if uid:
            user = User.objects.filter(pk=uid).first()
        else:
            user = User()
            # user.save()
        user.name = form.cleaned_data['name']
        user.email = form.cleaned_data['email']
        user.mobile = form.cleaned_data['mobile']
        user.us_adrs = form.cleaned_data['us_adrs']
        user.reg_day = form.cleaned_data['reg_day']
        user.save()


# ----------------- Универсальная форма товара --------------
def prdt_form(request, pid=None):
    form = ProductForm(request.POST, request.FILES)
    if form.is_valid():
        if pid:
            product = Product.objects.filter(pk=pid).first()
        else:
            product = Product()
        product.name = form.cleaned_data['name']
        product.content = form.cleaned_data['content']
        product.count = form.cleaned_data['count']
        product.price = form.cleaned_data['price']
        product.add_day = form.cleaned_data['add_day']
        product.image = form.cleaned_data['image']
        product.save()


# ----------------- Выбор клиента --------------
def choice_u(request):
    if request.method == 'POST':
        form = ChoiceUser(request.POST)
        if form.is_valid():
            return redirect(f'/ch_u/{form.cleaned_data["change"]}/')
    else:
        form = ChoiceUser()
        context = {
            "title": 'Выбор клиента',
            "head": 'Форма для выбора клиента',
            'form': form,
            'button': 'Выбрать'
        }
        return render(request, 'hw_app/form.html', context)


# ----------------- Выбор товара --------------
def choice_p(request):
    if request.method == 'POST':
        form = ChoiceProduct(request.POST)
        if form.is_valid():
            return redirect(f'/ch_p/{form.cleaned_data["change"]}/')
    else:
        form = ChoiceProduct()
        context = {
            "title": 'Выбор товара',
            "head": 'Форма для выбора товара',
            'form': form,
            'button': 'Выбрать'
        }
        return render(request, 'hw_app/form.html', context)
