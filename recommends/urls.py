from django.urls import path
from . import views

app_name = "recommends"

urlpatterns = [
    path("recommend/", views.all_recommends, name="recommend"),    
    path("recommend/create", views.CreateRecommendView.as_view(), name="create"),
    path("recommend/<int:pk>/edit", views.EditRecommendView.as_view(), name="edit"),
]