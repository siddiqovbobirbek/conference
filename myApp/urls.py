from django.urls import path
from .views import home, uz, ru, en

urlpatterns = [
    path("", home, name="home"),
    path("uz/", uz, name="uzbek"),
    path("ru/", ru, name="russian"),
    path("en/", en, name="english"),
]