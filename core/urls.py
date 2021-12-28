from django.urls import path
from projects import views as project_view
from django.conf.urls.static import static
from django.conf.urls import  include, url
from django.conf import settings


app_name = "core"

urlpatterns = [
   path("home", project_view.home_projects, name="project"),
   path("project", project_view.all_projects, name="project_list"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

