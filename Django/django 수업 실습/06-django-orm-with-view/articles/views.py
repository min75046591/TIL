from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles':articles
    }
    
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


def new(request):
    return render(request, 'articles/new.html')


def create(request):
# get 속성 값에 Query Dict 형태가 있음
# <QueryDict: {'title': ['제목'], 'content': ['내내내용']}> => 타이틀과 컨텐츠는 장고가 작성한게 아닌 우리가 작성한 것
    title = request.POST.get('title')
    content = request.POST.get('content')
    
    # 1
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()
    # 유효성 검사는 가능하나 2번이 더 간결함


    # 2     # 앞으로 계속 사용할 방법
    article = Article(title=title, content=content)
    # 유효성 검사 후 세이브가 되는거다.
    article.save()
    return redirect('articles:detail', article.pk)
    
    # 3
    # Article.objects.create(title=title, content=content)
    # return render(request, 'articles/create.html')
    # -> 유효성 검사 할 타이밍이 없다.


def delete(request, pk):
    # 몇번 글 삭제할건데? -> 조회를 먼저 해야함
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article':article,
    }
    return render(request, 'articles/edit.html', context)


def update(request, pk):
    # 몇번 게시글 수정? -> 조회 먼저 해야함
    article = Article.objects.get(pk=pk)

    title = request.POST.get('title')
    content = request.POST.get('content')

    article.title = title
    article.content = content
    article.save()

    return redirect('articles:detail', article.pk)