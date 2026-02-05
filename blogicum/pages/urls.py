from django.urls import path
import views

app_name = 'pages'

urlpatterns = [
    path('about/', views.about, name='about'),
    path('rules/', views.rules, name='rules'),
]
