from django.urls import path
from . import views

urlpatterns = [
    # 1. 사용자의 접속 화면
    #   - 정답 번호까지 확인 가능
    path('start/', views.start),
    # 2. 사용자의 추측
    path('guess/<int:session_id>/', views.guess),
]
