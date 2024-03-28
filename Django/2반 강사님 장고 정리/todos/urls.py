from django.urls import path
from . import views

app_name = 'todos'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('new/', views.new, name='new'),
    path('<int:pk>/', views.detail, name="detail"),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/complete/', views.complete, name='complete'),
    path('<int:pk>/start/edit', views.edit, name='edit'),
]