from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'sights'

urlpatterns = [
    #path('', views.landmark_list, name='landmark_list'),
    path('', views.LandmarkListView.as_view(), name='landmark_list'),
    path('propose/', views.landmark_propose, name='landmark_propose'),
    path('login/', views.user_login, name='login'),
    #path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('<name>/', views.landmark_detail, name='landmark_detail'),
]
