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

    path('orgs/', views.org_list, name='org_list'),
    path('orgs/add/', views.org_create, name='org_create'),
    path('orgs/<int:pk>/edit/', views.org_edit, name='org_edit'),
    path('orgs/<int:pk>/delete/', views.org_delete, name='org_delete'),

    path('education/', views.edu_list, name='edu_list'),
    path('education/add/', views.edu_create, name='edu_create'),
    path('education/edit/<int:pk>/', views.edu_edit, name='edu_edit'),
    path('education/delete/<int:pk>/', views.edu_delete, name='edu_delete'),

    path('projects/', views.project_list, name='project_list'),
    path('projects/add/', views.project_create, name='project_create'),
    path('projects/edit/<int:pk>/', views.project_edit, name='project_edit'),
    path('projects/delete/<int:pk>/', views.project_delete, name='project_delete'),
]

