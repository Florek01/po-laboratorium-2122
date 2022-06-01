from django.db import models

from .utils import create_new_ref_number


class CardType(models.TextChoices):
    DEBIT = 'Debit card'
    CREDIT = 'Credit card'

    def __str__(self):
        return self.name


class AccountType(models.TextChoices):
    PERSONAL = 'Personal account'
    SAVINGS = 'Savings account'
    FOREIGN = 'Foreign currency account'

    def __str__(self):
        return self.name


class Card(models.Model):
    card_number = models.CharField(max_length=16,
                                   blank=True,
                                   editable=False,
                                   unique=True,
                                   default=create_new_ref_number
                                   )
    card_type = models.CharField(choices=CardType.choices, max_length=50)

    def __str__(self):
        return '{} {}'.format(self.card_number, self.card_type)


class Account(models.Model):
    account_number = models.CharField(max_length=26,
                                      blank=True,
                                      editable=False,
                                      unique=True,
                                      default=create_new_ref_number
                                      )
    account_type = models.CharField(choices=AccountType.choices, max_length=50)
    balance = models.CharField(max_length=200)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {} {}'.format(self.account_number, self.account_type, self.balance)


class Address(models.Model):
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)


class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    pesel = models.CharField(max_length=11)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    accounts = models.ManyToManyField(Account)

    def __str__(self):
        return '{} {} {}'.format(self.first_name, self.last_name, self.pesel)
