from django import forms
from .models import Article

# 대표적으로 로그인 정보를 받을 때
# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)


class ArticleForm(forms.ModelForm):
    class Meta:
         # 어떤 모델과 연동?
        model = Article
        # 그 모델에서 어떤 필드를 쓸지?
        # fields = ('title', 'content')
        fields = '__all__'
        # exclude = ('title', )