from django.urls import path

from . import views

app_name = "art_auth"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index")
]
