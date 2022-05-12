from django.urls import path
from . import views

urlpatterns = [
    path('', views.month_list, name='month_list'),
    path('<int:month>/', views.monthly_challenge_num, name='month_num'),
    path('<str:month>/', views.monthly_challenge, name='month_val'),
]
