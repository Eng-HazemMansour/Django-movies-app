from django.urls import path
from .views import index, create, update, MovieList, CreateMovie, api_signup
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("", index),
    path("signup", api_signup),
    path("login/", obtain_auth_token),
    path("create/", create),
    path("list/", MovieList.as_view()),
    path("store/", CreateMovie.as_view()),
    path("update/<int:pk>", update.as_view()),
]