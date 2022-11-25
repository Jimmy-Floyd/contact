from django.urls import path
from . import views
urlpatterns = [
    path('', views.contacts, name='contacts'),
    path('/add_contact', views.add_contact, name='add_contact')
]