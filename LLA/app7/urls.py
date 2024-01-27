from django.urls import path
from . import views

urlpatterns=[
    path('show/',views.Sign_in)
]