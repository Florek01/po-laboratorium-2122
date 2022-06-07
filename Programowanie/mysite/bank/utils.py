import random


def create_new_account_number():
    return str(random.randint(10000000000000000000000000, 99999999999999999999999999))

def create_new_card_number():
    return str(random.randint(100000000000, 999999999999))

