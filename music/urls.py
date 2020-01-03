from django.urls import path
from . import views

app_name = 'music'
urlpatterns = [
    path('', views.home, name='home'),
    path('<int:album_id>/', views.detail, name='detail'),
]
