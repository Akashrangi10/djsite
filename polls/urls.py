from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("demo", views.dome, name="demo"),
    path("save_news", views.save_news, name="save_news")
]