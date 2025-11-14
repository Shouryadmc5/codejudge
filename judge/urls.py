from django.urls import path
from . import views

app_name = 'judge'

urlpatterns = [
    path('', views.problem_list, name='problem_list'),
    path('problem/<slug:slug>/', views.problem_detail, name='problem_detail'),
    path('register/', views.register, name='register'),
    path('submission/<int:pk>/', views.submission_result, name='submission_result'),
]
