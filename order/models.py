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
    address = models.CharField(blank=True, null=True, max_length=100)
    insurer_id = models.ImageField(blank=True, null=True, )


class OrderMenu(models.Model):

    CHOICE_TYPE = (
        ('rp', 'rp'),
        ('iv', 'iv'),
        ('doc', 'doc'),
        ('jihi_other', 'jihi_other'),
        ('txt', 'txt')
    )

    CHOICE_CATEGORY = (
        ('渡航ワクチン','渡航ワクチン'),
        ('美容健康注射','美容健康注射'),
        ('ビタミン剤','ビタミン剤'),
        ('一般ワクチン','一般ワクチン'),
        ('アフターピル・低用量ピル','アフターピル・低用量ピル'),
        ('美容薬品','美容薬品'),
        ('トラベル予防薬','トラベル予防薬'),
        ('ED治療薬','ED治療薬'),
        ('ヘルスチェック・健康診断','ヘルスチェック・健康診断'),
        ('疲労回復注射','疲労回復注射'),
        ('AGA治療薬','AGA治療薬'),
        ('その他・ご相談','その他・ご相談'),

    )

    CHOICE_IVTYPE = (
        ('静脈注射','静脈注射'),
        ('筋肉注射','筋肉注射'),
        ('皮下注射','皮下注射'),
        ('点滴注射','点滴注射'),
        ('皮内注射','皮内注射'),
        ('その他注射','その他注射'),
    )

    category = models.CharField(blank=True, null=True, max_length=50, choices=CHOICE_CATEGORY, unique=False, default='')
    name = models.CharField(blank=True, null=True, max_length=50)
    description = models.TextField(blank=True, null=True, max_length=100)
    price = models.IntegerField(blank=True, null=True, )
    code = models.CharField(blank=True, null=True, max_length=15)
    stock = models.IntegerField(blank=True, null=True, )
    type = models.CharField(blank=True, null=True, max_length=10, choices=CHOICE_TYPE, unique=False, default='')
    ivtype = models.CharField(blank=True, null=True, max_length=10, choices=CHOICE_IVTYPE, unique=False, default='')

class OrderDetail(models.Model):
    ptname = models.CharField(blank=True, null=True, max_length=50)
    kananame = models.CharField(blank=True, null=True, max_length=50)
    patientid = models.CharField(blank=True, null=True, max_length=20)
    felicaid = models.CharField(blank=True, null=True, max_length=30)
    ordername = models.CharField(blank=True, null=True, max_length=200)