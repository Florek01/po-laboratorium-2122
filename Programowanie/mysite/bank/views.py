
from django.http import HttpResponse
from .models import Account, Client, Card, Address
from django.template import loader
from django.shortcuts import render
from .forms import FormClient, FormAddress, FormAccount


def index(request):
    index_list = 'Account', 'Client', 'Form'
    template = loader.get_template('bank/index.html')
    context = {
        'index_list': index_list,
    }
    return HttpResponse(template.render(context, request))


def form(request):
    form_list = 'FormClient', 'FormAddress', 'FormAccount'
    template = loader.get_template('bank/form.html')
    context = {
        'form_list': form_list,
    }
    return HttpResponse(template.render(context, request))


def account(request):
    account_list = Account.objects.all
    template = loader.get_template('bank/account.html')
    context = {
        'account_list': account_list,
    }
    return HttpResponse(template.render(context, request))


def client(request):
    client_list = Client.objects.all
    template = loader.get_template('bank/client.html')
    context = {
        'client_list': client_list,
    }
    return HttpResponse(template.render(context, request))


def card(request):
    card_list = Card.objects.all
    template = loader.get_template('bank/card.html')
    context = {
        'card_list': card_list,
    }
    return HttpResponse(template.render(context, request))

def address(request):
    address_list = Address.objects.all
    template = loader.get_template('bank/address.html')
    context = {
        'address_list': address_list,
    }
    return HttpResponse(template.render(context, request))


def formClient(request):
    form = FormClient(request.POST or None)

    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, 'bank/formclient.html', context)


def formAddress(request):
    form = FormAddress(request.POST or None)

    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, 'bank/formaddress.html', context)


def formAccount(request):
    form = FormAccount(request.POST or None)

    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, 'bank/formaccount.html', context)