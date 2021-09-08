from django.urls import path

from . import views

app_name = 'order'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('select/', views.SelectView.as_view(), name='select'),
    
]