from django.db import models
from django.shortcuts import reverse

from django.utils.text import slugify
from time import time
def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))


# Create your models here.
class Transaction(models.Model):
    client = models.CharField(max_length=150, db_index=True)
    id_client = models.IntegerField(db_index=True)
    TYPE_TRANS = (
        (1, "Перевод физ. лицу"),
        (2, "Перевод перевод юр. лицу")
    )
    t_trans = models.IntegerField(choices=TYPE_TRANS)
    TYPE_CLIENT = (
        (1, "Брокер"),
        (2, "Кредитная карта"),
        (3, "Дебетовая карта"),
        (4, "Юридическое лицо"),
        (5, "Сберегательный счет"),
    )
    t_type = models.IntegerField(choices=TYPE_CLIENT)
    amount = models.IntegerField(db_index=True)
    currency = models.CharField(max_length=3)
    payer_bank_name = models.CharField(max_length=100)
    date_pub = models.DateTimeField(auto_now_add=True)
