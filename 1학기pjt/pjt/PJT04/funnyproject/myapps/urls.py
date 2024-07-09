from django.urls import path
from . import views

# 유지보수
app_name="myapps"
urlpatterns = [
    path('', views.index, name="index"),
]
