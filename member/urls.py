from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("list", views.list),
    path("css/register", views.css_register, name="css_member_register"),
    path("css/list", views.css_list),

]