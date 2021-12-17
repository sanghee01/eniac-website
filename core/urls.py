from django.urls import path
from projects import views as project_view

app_name = "core"

urlpatterns = [
   path("home", project_view.all_projects, name="project")
]