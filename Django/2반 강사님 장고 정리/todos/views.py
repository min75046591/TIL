from django.shortcuts import render, redirect
from .models import Todo
from .form import TodoForm

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    context = {
        'todos':todos,
    }
    return render(request, 'todos/index.html', context )


def create(request):
    title = request.POST.get('title')
    todo = Todo(title=title)    # 객체 생성 지점
    # 유효성 검사 할 곳
    # 유효하다면,
    todo.save()     # 생성 쿼리가 실행되는 곳

    return redirect('todos:index')


def new(request):
    form = TodoForm()   # 사용자에게 줄 form
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():     # form 으로 들어온 요청이 유효한가? -> 유효성 검사
            form.save()     # 새로운 row를 생성하는 sql 쿼리 실행
            return redirect('todos:index')
    context = {
        'form':form,
    }
    return render(request, 'todos/new.html', context)


def detail(request, pk):
    print('pk: ', pk)
    todo = Todo.objects.get(pk=pk)

    context = {
        'todo':todo,
    }
    return render(request, 'todos/detail.html', context)


def delete(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()       # 삭제 쿼리가 실행되는 곳

    return redirect('todos:index')


def complete(request, pk):
    todo = Todo.objects.get(pk=pk)
    # 토글이다. 스위치
    if todo.completed:  # if todo.completed == 1 일때 false로 바꾸고 수정
        todo.completed = False
    else:              
        todo.completed = True
    todo.save()     # 수정 쿼리 실행 시점

    return redirect('todos:index')


def edit(request, pk):
    todo = Todo.objects.get(pk=pk)
    if todo.is_editting:  # if todo.completed == 1 일때 false로 바꾸고 수정
        todo.is_editting = False
    else:              
        todo.is_editting = True # 화면에 input form 출력하기
    todo.save()
    return redirect('todos:index')