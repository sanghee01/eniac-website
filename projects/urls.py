from django.urls import path
from . import views

app_name = "project"

urlpatterns = [
    path("<int:pk>/", views.ProjectDetail.as_view(), name="detail"),
    path("<int:pk>/edit", views.EditProjectView.as_view(), name="edit"),
    path("/creates", views.CreateProjectView.as_view(), name="create"),
    path(
        "<int:room_pk>/projects/<int:project_pk>/delete/",
        views.delete_project,
        name="delete-project",
    ),
]