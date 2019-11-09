from django.urls import path
from . import views

app_name = 'sights'

urlpatterns = [
    #path('', views.landmark_list, name='landmark_list'),
    path('', views.LandmarkListView.as_view(), name='landmark_list'),
    path('<name>/', views.landmark_detail, name='landmark_detail'),
]
