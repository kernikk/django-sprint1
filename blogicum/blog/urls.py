from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    # Главная страница — список постов
    path('', views.index, name='index'),
    # Детальная страница поста, id — целое число
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    # Страница постов по категории, slug — строка/слаг
    path('category/<slug:category_slug>/', views.category_posts, name='category_posts'),
]