from django.urls import path
from projects import views as project_view
from django.conf.urls.static import static
from django.conf.urls import  include, url
from django.conf import settings
from django.urls import path
from . import views


app_name = "activity"

urlpatterns = [
 path("activity/<int:act_pk>", views.all_activity, name="activities"),
 path("creates", views.CreateChallengeView.as_view(), name="create"),
 path("createAct", views.CreateActivityView.as_view(), name="createAct"),
 path("<int:pk>/edit", views.EditActivityView.as_view(), name="edit"),
 path("<int:pk>", views.DetailActivity.as_view() , name="detail"),
 path('<int:pk>/comments/', views.comment_create, name='comments_create'),
 path('<int:pk>/delete', views.DeleteActivityView.as_view(), name='delete'),
 



 ]


