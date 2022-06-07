from django.contrib import admin
from .models import Address, Client, Account, Card

admin.site.register(Client)
admin.site.register(Account)
admin.site.register(Card)
admin.site.register(Address)
