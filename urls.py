from django.urls import path
from . import views

urlpatterns = [
    path("", views.person_list),
    path("list/", views.person_list),
    path("register/", views.register, name="register"),
    path("delete/", views.delete),
    path("update/", views.update, name="update"),

    path("translate/", views.translate, name="translate"),
    path("translate_papago/", views.translate_papago, name="translate_papago"),
]