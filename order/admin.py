from django.contrib import admin

# Register your models here.
from .models import OrderDetail, Patient, OrderMenu

admin.site.site_url = '/order'
admin.site.site_header = 'タッチパネルシステム管理画面'

class OrderMenuAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'price', 'code', 'type', 'ivtype')

class PatientAdmin(admin.ModelAdmin):
    list_display = ('fullname_kana', 'birthday', 'gender')

class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ('ptname', 'patientid', 'ordername')

admin.site.register(Patient ,PatientAdmin)
admin.site.register(OrderMenu, OrderMenuAdmin)
admin.site.register(OrderDetail, OrderDetailAdmin)