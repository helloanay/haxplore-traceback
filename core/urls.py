from django.urls import path, include
from core import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('auth/login/', views.user_login, name='auth-login'),
    path('auth/logout/', views.user_logout, name='auth-logout'),
    path('equipments/', views.equipments_list, name='equipments-list'),
    path('equipments/new/', views.equipment_new, name='equipments-new'),
]
