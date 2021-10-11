from django.urls import path

from . import views

app_name = 'order'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('input/', views.InputView.as_view(), name='input'),
    path('returnpt/', views.ReturnptView.as_view(), name='returnpt'),
    path('ic/', views.IcView.as_view(), name='ic'),
    path('select/', views.SelectView.as_view(), name='select'),
    
]