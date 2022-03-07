from django.urls import path
from . import views

app_name = "notice"

urlpatterns = [
    path("search/", views.search, name="search"),
    path("creates", views.CreateNoticetView.as_view(), name="create"),
    path("<int:pk>", views.NoticeDetail.as_view() , name="detail")
]