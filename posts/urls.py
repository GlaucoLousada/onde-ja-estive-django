from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.PostListView.as_view(), name='index'),
    path('posts/create/', views.PostCreateView.as_view(), name='create'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('posts/<int:pk>/update/', views.PostUpdateView.as_view(),
         name='update'),
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(),
         name='delete'),
    path('posts/<int:pk>/comment/', views.create_comment, name='comment'),
    path('categories/', views.CategoryListView.as_view(), name='categories'),
    path('categories/<int:pk>/', views.detail_category, name='category'),
]
