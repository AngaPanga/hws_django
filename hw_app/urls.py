from django.urls import path
from . import views


urlpatterns = [
    path('', views.general, name='general'),
    path('complete/', views.complete, name='complete'),
    path('fakes/<int:urs>/<int:pds>/<int:ods>/', views.fake_datas, name='fakes'),
    path('lu/', views.list_users, name='list_users'),
    path('lp/', views.list_products, name='list_products'),
    path('lo/', views.list_orders, name='list_orders'),
    path('basket/<int:oid>/', views.basket, name='basket'),
    path('us_pr/<int:uid>/', views.us_products, name='us_pr'),
    path('us_pr_tm/<int:uid>/<int:dif_day>/', views.us_products_time, name='us_pr_tm'),
    path('adds/', views.adds, name='adds'),
    path('add_u/', views.add_user, name='add_u'),
    path('add_p/', views.add_product, name='add_p'),
    path('ch_u/<int:uid>/', views.ch_user, name='ch_u'),
    path('ch_p/<int:pid>/', views.ch_product, name='ch_p'),
    path('cu/', views.choice_u, name='cu'),
    path('cp/', views.choice_p, name='cp'),
]
