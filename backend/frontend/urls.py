from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('project/<int:id>/', views.project_detail, name='project_detail'),
    path('single-portfolio.html', views.project_detail, name='project_detail'),

]
