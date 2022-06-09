from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('account/', views.account, name='account'),
    path('address/', views.address, name='address'),
    path('client/', views.client, name='client'),
    path('card/', views.card, name='card'),
    path('form/', views.form, name='form'),
    path('formclient', views.formClient),
    path('formaddress', views.formAddress),
    path('formaccount', views.formAccount),
]
