from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('project/<int:id>/', views.project_detail, name='project_detail'),
    path('login/', views.login_view, name="login"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('logout/', views.logout_view, name="logout"),
    path('profiles/', views.profile_list, name='profile-list'),
    path('profiles/add/', views.profile_add, name='profile-add'),
    path('profiles/<int:pk>/edit/', views.profile_edit, name='profile-edit'),
    path('profiles/<int:pk>/delete/', views.profile_delete, name='profile-delete'),

    path('skills/', views.skill_list, name='skill_list'),
    path('skills/add/', views.skill_create, name='skill_create'),
    path('skills/<int:pk>/edit/', views.skill_edit, name='skill_edit'),
    path('skills/<int:pk>/delete/', views.skill_delete, name='skill_delete'),
]

