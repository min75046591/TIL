# PJT-06 (영화)

## 민수와 희진이의 프로젝트!

### 민수

- movies 앱 만들기

### 희진

- accounts 앱 만들기

**나눈 기준**

- 서로가 어려워하는 파트를 구분

---

# GIT

## 브랜치

- 우리는 앱을 기준으로 나누어서 작업을 하였고, 브랜치를 각각 하나만 만들어서 관리했다.
- 각자의 브랜치를 만들어서 서로의 공간에서 작업을 하였다.
- 중간중간 master에 옮기고, merge를 해주었다.

### 어려웠던점

- 충돌
    - 같은 파일을 작업하면 merge시 충돌이 일어났다.
    - vscode에서 편리하게 지원을 해주어 빠르게 해결할 수 있었다.

### 배운점

- 하나의 프로젝트를 진행할 때 각자의 브랜치에서 프로젝트를 구현하고 merge를 통해 각자 진행한 사항을 합쳐 프로젝트를 만들었다.
- 협업을 할때 왜 깃을 사용하는지 알 수 있었다.
- 깃은 엄청난 협업툴이다!

---

# PJT

## movies - 민수

- 배운점

1. 이번 프로젝트를 진행하면서 내가 맡은 부분인 movies 앱을 구현하며 좋아요 부분과 models에서
ManyToManyField를 설정 하는 부분에 대해 잘 알게 됐다. 

    - models의 like_user 부분에서 related_name을 설정해주지 않아서 충돌이 일어났었다.

    - like_user필드 생성 시 자동을로 역참조 매니저 .movie_set가 생성 되어 이전 movie-user 관계와 같은 이름의 매니저를 사용하여 충돌이 발생. 이로 인해 user가 작성한 글(user.movie_set)과 user가 좋아요를 누른 글(user.movie_set)을 구분할 수 없게 됐다.

```python
class Movie(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = 'like_movies')
    # 필요 시 related_name 설정



class Comment(models.Model):
    content = models.CharField(max_length=30)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

```

index.html에서 좋아요 수 표현

```python
<a href="{% url "movies:detail" movie.pk %}">DETAIL</a>
    <p>좋아요 : {{movie.like_user.all|length}}</p>
    <form action="{% url "movies:likes" movie.pk %}" method='POST'>
        {% csrf_token %}
        {% if request.user in movie.like_user.all %}
          <input type="submit" value='좋아요 취소'>      
        {% else %}
          <input type="submit" value='좋아요'>
        {% endif %}
      </form>
```

view에서 좋아요 구현

```python
# 좋아요 기능 구현
def likes(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.user in movie.like_user.all():
        movie.like_user.remove(request.user)
    else:
        movie.like_user.add(request.user)
    return redirect('movies:index')

```
이미 있다면 remove. 없다면 add를 통해 좋아요 추가! 이를 index.html의 좋아요 기능과 결합하여 이미 있다면 좋아요 취소 버튼을 보여주고 좋아요를 누르지 않았다면, 좋아요 버튼을 보여줌!


&nbsp;


---

## accounts - 희진

### 1. 회원 가입

**form**

- UserCreationForm - 회원가입시 사용자 입력 데이터를 받는 built-in ModelForm
- get_user_model - 현재 활성화된 User 모델을 반환하며, 그렇지 않은 경우 User(default) 모델을 반환한다.
- 회원가입에서 사용하는 form은 기존 유저 모델로 인해 작성된 클래스이기에 대체한 유저 모델로 변경이 필요하다
    
    ```python
    from django.contrib.auth import get_user_model
    from django.contrib.auth.forms import UserCreationForm, UserChangeForm
    
    class CustomUserCreationForm(UserCreationForm):
        class Meta(UserCreationForm.Meta):
            model = get_user_model()
    ```
    

**views**

- 위에서 만든 form을 로드해온다
- if request.user.is_authenticated: 를 통해서 로그인이 되어 있다면 다른 페이지로 넘겨준다.
- 그것이 아니라면 회원가입을 할 수 있도록 해준다.

```python
def signup(request):
    if request.user.is_authenticated:
        return redirect('movies:index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movies:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form':form,
    }
    return render(request,'accounts/signup.html',context)
```

### 2. 회원 정보 수정

**from**

- UserChangeForm() - 회원정보 수정 시 사용자 입력 데이터를 받는 폼
- 모든 정보를 수정하지 않도록 일반 사용자들이 수정할 값들만 출력이 되도록 해야한다.
    - fields로 받을 정보

```python
class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('first_name','last_name','email',)
```

**view**

- view함수 작성시 CustomUserChangeForm에는 instance값으로 request.user값이 들어가야 한다.

```python
@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            return redirect('movies:index')
    else:
        form = CustomUserChangeForm(instance = request.user)
    context = {
        'form':form,
    }
    return render(request, 'accounts/update.html',context)
```

### 3. 비밀번호 변경

- PasswordChangeForm() - 비밀번호 변경 시 사용자 입력 데이터를 받는 폼
- PK값이 필요하다.

**view**

```python
@login_required
def change_password(request,pk):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user)
            return redirect('movies:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form' : form,
    }
    return render(request, 'accounts/change_password.html',context)
```

- update_session_auth_hash - 암호 변경 시 기존 세션을 자동으로 갱신
    - 만약 POST요청이고, 해당 값의 is_vaild 검증이 통과되면, 저장해 준 후 update_session_auth_hash를 해준다

### 4. 로그인

- AuthenticationForm() - 로그인 인증에 사용할 데이터를 입력받는
- login(request,user) - AuthenticationForm을 통해 인증된 사용자를 로그인 해줌
- get_user() - AuthenticationForm의 인스턴스 메서드
    - 유효성 검사를 통과했을 경우 로그인 한 사용자 객체를 반환

```python
def login(request):
    if request.user.is_authenticated:
        return redirect('movies:index')
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request,form.get_user())
            return redirect('movies:index')
    else:
        form = AuthenticationForm()
    context = {
        'form':form,
    }
    return render(request,'accounts/login.html',context)

```

### 5. 로그아웃

- logout(request)

```python
def logout(request):
    auth_logout(request)
    return redirect('movies:index')
```

### 6. 프로필 페이지

- get_user_model - 현재 활성화된 User 모델을 반환하며, 그렇지 않은 경우 User(default) 모델을 반환한다.
- 넘겨받은 pk값을 통해 해당 페이지로 접근

```python
    User = get_user_model()
    person = User.objects.get(username=username)
    context = {
        'person':person,
    }
    return render(request,'accounts/profile.html',context)
```

### 7. follow

- 초장기 모델은 손을 댈 부분이 없었다.
- 하지만 팔로워 부분이 들어오면서 추가로 작성할 부분이 생겼다.
- 팔로워
    - M:N관계이다.
    - 회원은 0명 이상의 팔로워를 가질 수 있고, 0명 이상의 다른 회원들을 팔로잉 할 수 있다.
    - 장고의 ManyToManyField()를 사용했다.
    
    ```jsx
    class User(AbstractUser):
        followings = models.ManyToManyField('self',symmetrical=False, related_name = 'followers')
    ```
    
    - 참조
        - 내가 팔로우 하는 사람들 - 팔로잉
    - 역참조
        - 내가 팔로워가 되는 것 - 팔로워
    
    **관계조회시 편한방향으로 정해야 한다.**
    