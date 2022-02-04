from django.urls import path
from projects import views as project_view
from notices import views as notice_view
from activities import views as activity_view
from recommends import views as recommend_view
from django.conf.urls.static import static
from django.conf.urls import  include, url
from django.conf import settings


app_name = "core"

urlpatterns = [
   path("", project_view.home_projects, name="project"),
   path("project", project_view.all_projects, name="project_list"),
   path("notice", notice_view.all_notice, name="notice_list"),
   path("activity", activity_view.all_activity, name="activity_list"),
   path("recommend", recommend_view.all_recommends, name="recommend_list"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

