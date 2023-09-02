from django import forms
from .models import *


class UserForm(forms.Form):
    name = forms.CharField(max_length=100, label='Имя')
    email = forms.EmailField(label='E-mail')
    mobile = forms.CharField(max_length=20, label='Моб. тел.')
    us_adrs = forms.CharField(max_length=100, label='Адрес')
    reg_day = forms.DateField(label='Дата регистрации',
                              widget=forms.DateInput(attrs={'type': 'date'}))


class ProductForm(forms.Form):
    name = forms.CharField(max_length=100, label='Название')
    add_day = forms.DateField(label='Дата добавления',
                              widget=forms.DateInput(attrs={'type': 'date'}))
    price = forms.DecimalField(label='Цена', widget=forms.NumberInput())
    count = forms.IntegerField(label='Кол-во', widget=forms.NumberInput())
    image = forms.ImageField()
    content = forms.CharField(max_length=1000, label='Описание', widget=forms.Textarea())



class ChoiceUser(forms.Form):
    change = forms.ChoiceField(choices=[(el.id, el) for el in User.objects.all()])


class ChoiceProduct(forms.Form):
    change = forms.ChoiceField(choices=[(el.id, el) for el in Product.objects.all()])
