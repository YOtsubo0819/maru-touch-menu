from django.contrib import admin

# Register your models here.
from .models import OrderDetail, Patient, OrderMenu

class OrderMenuAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'price', 'code')

class PatientAdmin(admin.ModelAdmin):
    list_display = ('fullname_kana', 'birthday', 'gender')

class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ('ptname', 'patientid', 'ordername')

admin.site.register(Patient ,PatientAdmin)
admin.site.register(OrderMenu, OrderMenuAdmin)
admin.site.register(OrderDetail, OrderDetailAdmin)