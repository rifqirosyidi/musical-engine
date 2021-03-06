from django.urls import path
from . import views

app_name = 'music'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('album/create/', views.AlbumCreate.as_view(), name='album-create'),
    path('album/<int:pk>/update/', views.AlbumUpdate.as_view(), name='album-update'),
    path('album/<int:pk>/delete/', views.AlbumDelete.as_view(), name='album-delete'),
]
