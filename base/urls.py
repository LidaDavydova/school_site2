from django.urls import path
from . import views
from .views import *

app_name = 'base'

urlpatterns = [
    path('', views.base, name="base"),
    path('info/', views.info, name="info"),
    path('subject/', views.subject, name="subject"),
    path('club/', views.club, name="club"),
    path('math/', views.math, name="math"),
    path('informatics/', views.informatics, name="informatics"),
    path('physics/', views.physics, name="physics"),
    path('chemistry/', views.chemistry, name="chemistry"),
    path('projects/', Projects.as_view(), name="projects"),
    path('add_project/', Add_project.as_view(), name="add_project"),
    path('account/login/', views.login_user, name='login'),
    path('account/profile/', views.profile, name='profile'),
    path('account/register/', RegisterView.as_view(), name='register'),
    path('logout/', Logout.as_view(), name='logout'),
]