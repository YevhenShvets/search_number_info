from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search_form, name='search_form'),
    path('search/<str:number>/', views.search, name='search_number'),
]
