from django.urls import path
from . import views

# ULRConf
urlpatterns = [
    path('hello/', views.say_hi)
]