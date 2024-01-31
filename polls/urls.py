from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name= "detail"),
    path("<int:question_id>/results/", views.results, name= "results"),
    path("<int:question_id>/vote/", views.vote, name= "vote"),
    path("register_view/", views.register_view, name= "register_view"),
    path("login_view/", views.login_view, name= "login_view"),
    path("logout_view/", views.logout_view, name= "logout_view"),
]