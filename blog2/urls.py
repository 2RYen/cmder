from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("form1/write", views.post2_write, name="post2_write"),
    path("form1/write_css", views.post2_write_css, name="post2_write_css"),

    path("form1/list", views.post2_list),
    path("form1/list_css", views.post2_list_css),
]