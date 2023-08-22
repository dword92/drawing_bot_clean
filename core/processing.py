from random import randint, choices
from faker import Faker
import datetime
import random

fake = Faker(locale="ru_RU")
chars = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'И', 'К', 'О', 'Р']


def genering():
    initials = ". ".join(choices(chars, k=2))
    id_transaction = randint(17871000010, 17987654399)
    file_name = randint(10, 99)
    status_bar_time = datetime.datetime.now().strftime("%H:%M")
    date_time = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
    my_name = f"{fake.last_name()} {initials}."
    return id_transaction, file_name, status_bar_time, date_time, my_name


def format_numbers(phone):
    numbers = list(filter(str.isdigit, phone))[1:]
    ff = "+7 ({}{}{}) {}{}{}-{}{}-{}{}".format(*numbers)
    return ff
