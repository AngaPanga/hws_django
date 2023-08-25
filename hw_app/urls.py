from django.urls import path
from . import views


urlpatterns = [
    path('', views.general, name='general'),
    path('cfu/', views.create_fake_users, name='create_users'),
    path('cfp/', views.create_fake_products, name='create_products'),
    path('cfo/', views.create_fake_orders, name='create_orders'),
    path('lfu/', views.list_fake_users, name='list_users'),
    path('lfp/', views.list_fake_products, name='list_products'),
    path('lfo/', views.list_fake_orders, name='list_orders'),
]