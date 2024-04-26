from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('save-data/', views.save_data, name='save_data'),
]

# 민수야 죽을래?
# 잘 하 자?
# 내가 뭐라 했어
# URl -> view (-> template ) 하라 해 ㅆ지 ?
# 김민수 
# 잘 해 라 . . 
# 내 마지막 조언이다 . . . ㅡㅡ^
