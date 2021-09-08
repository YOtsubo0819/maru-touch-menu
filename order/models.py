from django.db import models
from django.db.models.base import Model

# Create your models here.

class Patient(models.Model):
    fullname_kana = models.CharField(max_length=50)
    fullname_kanji = models.CharField(max_length=50)
    birthday = models.DateField()
    gender = models.CharField(max_length=5)
    patientid = models.IntegerField(blank=True, null=True, )
    tel_number = models.CharField(max_length=13)
    postal_code = models.CharField(max_length=8)
    address1 = models.CharField(blank=True, null=True, max_length=100)
    address1 = models.CharField(blank=True, null=True, max_length=100)
    insurer_id = models.ImageField(blank=True, null=True, )


class OrderMenu(models.Model):

    CHOICE_TYPE = (
        ('rp', 'rp'),
        ('iv', 'iv'),
        ('doc', 'doc'),
        ('jihi_other', 'jihi_other'),
        ('txt', 'txt')
    )

    category = models.CharField(blank=True, null=True, max_length=50)
    name = models.CharField(blank=True, null=True, max_length=50)
    description = models.TextField(blank=True, null=True, max_length=100)
    price = models.IntegerField(blank=True, null=True, )
    code = models.CharField(blank=True, null=True, max_length=15)
    stock = models.IntegerField(blank=True, null=True, )
    type = models.CharField(blank=True, null=True, max_length=10, choices=CHOICE_TYPE, unique=True, default='')

class OrderDetail(models.Model):
    ptname = models.CharField(max_length=50)
    patientid = models.CharField(max_length=20)
    felicaid = models.CharField(max_length=30)
    ordername = models.CharField(max_length=200)