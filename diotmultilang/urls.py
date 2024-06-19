from django.urls import path

from . import views

app_name = "diotmultilang"
urlpatterns = [
    path("", views.index, name="index")
]