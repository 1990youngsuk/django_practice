from django.urls import path

from . import views

urlpatterns = [
    path("<int:number>", views.number, name="number"),
    path("<str:name>", views.greet, name="greet"),
    path("", views.index, name="index"),
]
