from django.urls import path
from . import views

app_name = "recommends"

urlpatterns = [
    path("recommend/", views.all_recommends, name="recommend"),
]