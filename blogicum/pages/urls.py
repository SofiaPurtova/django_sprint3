from django.urls import path
from pages import views  # Импорт views из текущего приложения

app_name = 'pages'  # Пространство имён

urlpatterns = [
    path('about/', views.about, name='about'),  # Страница "О нас"
    path('rules/', views.rules, name='rules'),  # Страница "Правила"
]
