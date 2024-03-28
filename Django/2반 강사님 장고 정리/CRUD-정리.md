# CRUD 정리

과목: Django

<aside>
💡 주어진 스켈레톤과 제공된 요구사항에만 따라 프로젝트를 진행하며 발생할 수 있는 완성 코드의 목적과 구성 형태에 대한 이해도를 높이기 위함

</aside>

# 프로젝트 시작하기

## 프로젝트를 시작할 때 개발자가 고려해야할 사항

<aside>
💡 **기획자의 유무**

- 서비스를 구성할 때, 기획자 또는 PM 이 구성한 WBS와 기획에 따라 프로젝트를 구성할테지만, 작성되는 코드와 구성되는 프로젝트의 골격에 분명한 이유가 있어야한다.
</aside>

### 가정

1. 1인 개발자로서 기획 부터 개발까지 단독으로 진행한다. 
2. 서비스 주제 : Todo 애플리케이션 구성하기. 

## 기본적인 프로젝트 골격 구성

- 프로젝트 시작
    - 원하는 경로에서 프로젝트 폴더를 생성한다

```bash
mkdir todo-application
cd todo-application
python -m venv venv
source venv/Scripts/activate
pip install django 
pip freeze > requirements.txt

# django project 생성 

django-admin startproject config .

# project 정상 작동 여부 확인 
python manage.py migrate  # django에서 기본적으로 가지고 있는 내장 DB 테이블 생성
python manage.py runserver

# project 생성 
python manage.py startapp todos
```

- 생성한 `app` 을 생성한 프로젝트에서 사용하기 위해 `config/settings.py` 에 등록한다.

## CRUD 작성

- CRUD 구현 전 필요한 model class 를 먼저 구현한다.
    - todo
        
        ```python
        from django.db import models
        
        # Create your models here.
        
        class Todo(models.Model):
            title = models.CharField(max_length=200)
            completed = models.BooleanField(default=False)
            created_at = models.DateTimeField(auto_now_add=True)
        
        ```
        
        - 작상한 모델 마이그레이션
            
            ```bash
            python manage.py makemigrations
            python manage.py migrate
            ```
            
            - 위 명령어의 수행 시점?
                - 모델을 수정했다고 해서 반드시 위 명령어를 수행해야된다는 법칙은 없다.
                - 그럼 언제?
                    - 사용하는 app에 작성한 모델에 수정 사항이 있고, 그 수정 사항를 사용중인 데이터베이스에 적용하려고 할 때. 입력하는 명령어
                - 명령어 수행 후 사용 중인 데이터 베이스에 테이블이 정상적으로 작성됐는지 꼭 확인하자.
                    - table 이름 규칙
                        - `앱이름_모델이름`

### 개발 순서?

<aside>
💡 기본적인 CRUD 기능을 구현하려 할 때 어떤 순서로 시작해야 할까?

- **사실 반드시 따라야하는 순서는 없다**
    1.  admin 사이트를 활용하여 dummy data 만들기
    2. create를 먼저 구현 및 데이터 생성 
</aside>

- 장고가 제공해주는 관리자 사이트를 활용해서 dummy data 를 만드는 방향으로 선택해보자.
    - 관리자 계정 생성
        
        ```bash
        python manage.py createsuperuser
        ```
        

- DB 에 row 가 정상 생성 됐는지 확인!

### 인덱스 페이지 구현

- config/ursl.py
    - 경로에 `include` 를 사용하는 이유?
        - 앞으로 작성될 많은 앱, 그리고 작성될 많은 요청 경로를 하나의 파일에서 모두 관리하기 어려움으로 각 앱 [urls.py](http://urls.py) 로 요청을 나누어 별도로 관리할 수 있도록 해줌.
            
            ```python
            from django.contrib import admin
            from django.urls import path, include
            
            urlpatterns = [
                path("admin/", admin.site.urls),
                path("", include("todos.urls")),
            ]
            ```
            
- todos/urls.py
    - app은 기본적으로 [urls.py](http://urls.py) 파일을 생성해 주지 않음. → 직접 만들어야 함.
        - 아래, 초기 형태를 잡아준다.
        - 중요한 것은 [urls.py](http://urls.py) 를 정의 후 아무런 요청 경로를 작성하지 않더라도 반드시 `urlpatterns`  라는 빈 리스트를 정의해두어야 한다. `(안하면 오류 발생해요)`
        
        ```python
        from django.urls import path, include
        from . import views
        
        urlpatterns = []
        ```
        
- TODO 앱의 메인 페이지 (index) 작성하기.
- todos/urls.py
    
    ```python
    from django.urls import path, include
    from . import views
    
    app_name = "todos"
    
    urlpatterns = [
        path("", views.index, name="index"),
    ]
    ```
    
- todos/views.py
    
    ```python
    from django.shortcuts import render
    from .models import Todo
    
    # Create your views here.
    
    def index(request):
        todos = Todo.objects.all()
        context = {
            "todos": todos
        }
        # 정상적으로 랜더링 되는지 먼저 테스트 해보고
    		#  return render(request, "todos/index.html")
        return render(request, "todos/index.html", context)
    
    ```
    
    - todos/templates/todos/index.html
        
        ```html
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <meta http-equiv="X-UA-Compatible" content="ie=edge">
            <title>TODO INDEX</title>
        </head>
        <body>
            <h1>TODO INDEX</h1>
        </body>
        </html>
        ```
        
        - 화면 출력 확인!!!
        - 불러온 todos 를 화면에 출력
        
        ```html
        <ul class="list-group">
            {% for todo in todos %}
                <li class="list-group-item d-flex justify-content-between align-items-center">
                    <a href="{% url 'todos:detail' todo.pk %}">{{ todo.title }}</a>
        
                    <span>
                        {% if todo.completed %}
                            <span class="">완료</span>
                        {% else %}
                            <span class="">미완료</span>
                        {% endif %}
                        <form action="{% url 'todos:complete' todo.pk %}" method="post">
                            {% csrf_token %}
                            <button type="submit" class="btn btn-sm btn-outline-primary">Toggle</button>
                        </form>
                    </span>
                </li>
            {% endfor %}
        </ul>
        ```
        

### 베이스.html 만들기

- 생각해 보니, 나중에 앱이 늘어났을 때, 하다못해 todos 에서도 공통으로 사용될 html 코드가 많다고 판단이 된다. base.html 을 사용하도록 설정하자.
    
    ```python
    TEMPLATES = [
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": [BASE_DIR / "templates"],
            "APP_DIRS": True,
            "OPTIONS": {
                "context_processors": [
                    "django.template.context_processors.debug",
                    "django.template.context_processors.request",
                    "django.contrib.auth.context_processors.auth",
                    "django.contrib.messages.context_processors.messages",
                ],
            },
        },
    ]
    ```
    
    - base_dir/templates/base.html
    - bootstrap cdn 추가는 자유롭게. 시간 보고
    
    ```python
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    </head>
    <body>
    
    {% block content %}
    {% endblock content%}
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
    </body>
    </html>
    ```
    
    ### index.html 수정
    
    - `{% extends "base.html" %}` 는 항상 첫번째 줄에
    
    ```python
    {% extends "base.html" %}  
    
    {% block content %}
    <div class="container">
        <h1 class="h1">My Todos</h1>
        <hr class="w-100"/>
        <div class="row">
            <div class="col-md-6">
                <form action="#" method="post">
                    <div class="form-group mb-2">
                        <input type="text" name="title" class="form-control" placeholder="Enter a new todo" required>
                    </div>
                    <button type="submit" class="btn btn-primary">Add</button>
                </form>
            </div>
        </div>
    </div>
    {% endblock content %}
    ```
    
    - 인덱스 페이지에서 새로 만들기 기능 구현 연습 form 사용하지 않고
    
    ```html
    <form action="{% url 'todos:create' %}" method="post">
        {% csrf_token %}
        <div class="form-group mb-2">
            <input type="text" name="title" class="form-control" placeholder="Enter a new todo" required>
        </div>
        <button type="submit" class="btn btn-primary">Add</button>
    </form>
    ```
    
    ```python
    path("create/", views.create, name="create"),
    ```
    
    ```python
    def create(request):
        title = request.POST.get("title")
        todo = Todo(title=title)
        todo.save()
    
        return redirect("todos:index")
    ```
    
    - index.html
        - 만약 create 페이지를 별도로 또 두기
            - a tag 의 기본 요청은 `GET`
            
            ```html
            
            {% extends "base.html" %}
            
            {% block content %}
            <div class="container">
                <h1 class="h1">My Todos</h1>
                <hr class="w-100"/>
                <a href="{% url 'todos:create' %}" class="btn btn-primary">Create Todo</a>
            </div>
            {% endblock content %}
            ```
            
            - new.html
            
            ```python
            {% extends "base.html" %}
            
            {% block content %}
            <div class="container">
                <h1 class="h1">My Todos</h1>
                <a href="{% url 'todos:new' %}" class="btn btn-primary">할 일 생성 페이지</a>
                <hr class="w-100"/>
                <div class="row">
                    <div class="col-md-6">
                        <form action="{% url 'todos:create' %}" method="post">
                            {% csrf_token %}
                            <div class="form-group mb-2">
                                <input type="text" name="title" class="form-control" placeholder="Enter a new todo" required>
                            </div>
                            <button type="submit" class="btn btn-primary">Add</button>
                        </form>
                    </div>
                </div>
                </div>
            {% endblock content %}
            
            ```
            
            ```python
            # urls.py
            path("new/", views.new, name="new"),
            
            ```
            
            - todos.forms
            
            ```python
            from django import forms
            from .models import Todo
            
            class TodoForm(forms.ModelForm):
            
                class Meta:
                    model = Todo
                    fields = ("title",)
            
            ```
            
            - views form 사용하기.
            
            ```python
            from .forms import TodoForm
            
            def new(request):
                form = TodoForm()
                if request.method == "POST":
                    form = TodoForm(request.POST)
                    if form.is_valid():
                        form.save()
                        return redirect("todos:index")
                context = {
                    "form": form
                }
                # return render(request, "todos/new.html")    
                return render(request, "todos/new.html", context)
            
            ```
            
    
    ```python
    # urls.py
    path("new/", views.new, name="new"),
    
    # views.py
    def new(request):
        form = TodoForm()
        if request.method == "POST":
            form = TodoForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("todos:index")
        context = {
            "form": form
        }
        return render(request, "todos/new.html", context)
    ```
    
    ## 상세 페이지 이동 기능
    
    - index.html 에 a 태그 추가.
    
    ```html
    <li class="list-group-item d-flex justify-content-between align-items-center">
    	<a href="{% url 'todos:detail' todo.pk %}">{{ todo.title }}</a>
    	</li>
    
    ```
    
    - detail.html
        
        ```python
        {% extends "base.html" %}
        
        {% block content %}
        <a href="{% url 'todos:index' %}" class="btn btn-primary">Back</a>
        <div class="container">
            <h1 class="h1">{{ todo.title }}</h1>
          <h3 class="h3">{{ todo.created_at }}</h3>
            <hr class="w-100"/>
            <div class="row">
                <div class="col-md-6">
                  완료 여부 : {{ todo.completed}}
                </div>
            </div>
        </div>
        
        {% endblock content %}
        
        ```
        

### 완료 여부 토글 기능

<aside>
💡 **하나의 기능을 만들 때 어떤식으로 사용자의 사용을 유도할 것인지 우리는 항상 생각해야한다.**

</aside>

- 두 가지 선택이 있을 수 있을 것 같다.
    - 사용자가 등록한 할 일의 완료 여부를 계속 바꿀 수 있다.
    - 사용자가 등록한 할 일의 완료 여부 변경을 딱 한번만 수행할 수 있다.
        - False to True
- index.html

```python
                {% for todo in todos %}
                    <li class="list-group-item d-flex justify-content-between align-items-center">
                        <a href="{% url 'todos:detail' todo.pk %}">{{ todo.title }}</a>

                        <span>
                            {% if todo.completed %}
                                <span class="">완료</span>
                            {% else %}
                                <span class="">미완료</span>
                            {% endif %}
                            <form action="{% url 'todos:complete' todo.pk %}" method="post">
                                {% csrf_token %}
                                <button type="submit" class="btn btn-sm btn-outline-primary">Toggle</button>
                            </form>
                        </span>
                    </li>
                {% endfor %}
```

```python

# urls.py
path("complete/<int:todo_id>/", views.complete, name="complete"),

# views.py
def complete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    if todo.completed:
        todo.completed = False
    else:
        todo.completed = True

    todo.save()
```

### 할일 삭제

```python
# urls.py

path("delete/<int:todo_id>/", views.delete, name="delete"),

# vies.py

def delete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()

    return redirect("todos:index")
```

- 마지막으로 Update 기능은 Modelform을 사용해서 각자 구현해 봅시다 !