from django.contrib import admin
from .models import Client, Account, Card

admin.site.register(Client)
admin.site.register(Account)
admin.site.register(Card)

