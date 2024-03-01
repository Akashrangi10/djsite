from django.urls import path
from . import views

urlpatterns = [
    path("", views.core_index_view, name="core_index_view"),
]