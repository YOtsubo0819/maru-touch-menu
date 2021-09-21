from django.urls import path

from . import views

app_name = 'order'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('returninput/', views.ReturninputView.as_view(), name='returninput'),
    path('newinput/', views.NewinputView.as_view(), name='newinput'),
    path('gocounter/', views.GocounterView.as_view(), name='gocounter'),
    path('returnpt/', views.ReturnptView.as_view(), name='returnpt'),
    path('select/', views.SelectView.as_view(), name='select'),
    
]