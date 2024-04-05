# PJT 04 - 영화


## 이번 pjt를 통해 배운 내용
- 전체적인 웹페이지 구현에 대해 백과 프론트 다 구현하여 아직 view 함수 작성 부분과 forms나 model에서 model을 import하는 과정에 부족함을 느꼈다.

- 부트 스트랩을 장고에 어떻게 적용해서 css를 입힐지에 대해 검색하고 찾아보며 알게 되었다.

- 장고 다큐먼트를 참고해서 웹사이트를 구현하는데 어려움이 많았다. 우선 내가 필요한 부분을 찾는데 시간이 굉장히 오래 걸렸다. 제대로 장고 다큐먼트에서 찾으려고 들어간건 이번이 처음이라 낯설고 어려웠지만 친해질 필요를 느꼈다.

- 처음엔 구조 부분을 만들고 바로 CSS까지 입혀서 진행하려 했지만 머리가 더 복잡하고 구조가 머리속에서 잊혀져서 다음 과정을 진행하는데 어려움을 겪었다. 그래서 중간에 멈추고 구조를 먼저 다 짜고 css를 입히니 훨씬 편하고 진행도 수월했다. 이번 프로젝트 경험으로 구조를 먼저 잡고 기능을 구현 한 후에 css를 입혀야 한다고 아주 크게 느꼈다..!

- 잊고 있던 부트스트랩 사용법을 몸으로 고통 받으며 다시 상기 시킬 수 있었다. 하지만 프론트 백 둘다 많이 부족하다고 느껴서 주말에 시간이 날 때 마다 나만의 웹페이지 구현을 해보면서 연습을 해야겠다고 생각했다.

<hr>

````html
{% load django_bootstrap5 %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    {% bootstrap_css %}
    {% bootstrap_javascript %}
</head>

````

> 부트스트랩을 가상환경에서 다운 받고 적용을 할 때 사용한 코드이다.

- 이 코드를 사용하면 부트 스트랩을 html에 적용할 때 link와 script를 붙이지 않고 사용할 수 있다.

<br>

~~~~html
from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:movie_pk>/delete/', views.delete, name='delete'),
]
~~~~

- delete와 update에서 pk값에 문제가 생겨서 고생을 많이 했었다.

<br>

~~~~html
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name',)
        

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name', 'username',)

~~~~

#### account에서 폼을 작성하는 부분이 어려웠다. 또한 accounts의 views에서 혼자 작성하는게 거의 없었다. 이 부분에 대한 공부를 통해 많이 보완해 나가야 한다고 크게 느꼈다..

<br>

~~~~html
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash

~~~~

- 계정 views에서 import 해와야 하는 것들!

#### 장고와 부트스트랩을 결합하며 웹페이지를 구현하면서 웹 구축에 재미를 느꼈다. 하지만 그와 반대로 절망감도 많이 느꼈다. 꾸준히 알고리즘과 웹 공부를 하면서 더 많이 공부하고 더 많이 노력해서 단단한 베이스를 만들어야 한다고 느꼈다. '나를 죽이지 못하는 나를 더 강하게 만든다!' 항상 머리속에 새기면서 힘들고 괴롭더라도 빛날 미래를 위해 열심히 정진하겠다!