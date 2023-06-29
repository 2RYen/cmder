from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("form1/", views.post_list),
    path("form1/list", views.post_list),
    path("form1/write", views.post_write1, name="post_form1"),

    path("form2/", views.post_list),
    path("form2/list", views.post_list),
    path("form2/write", views.post_write2, name="post_form2"),

]
