from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.list_posts, name='index'),
    path('posts/create/', views.create_post, name='create'),
    path('posts/<int:pk>/', views.detail_post, name='detail'),
    path('posts/<int:pk>/update/', views.update_post, name='update'),
    path('posts/<int:pk>/delete/', views.delete_post, name='delete'),
]
