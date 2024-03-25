from django.db import models

# class 이름의 첫문자는 항상 "대문자"로 작성
# Model는 class이고, models는 모듈이다.
# 즉, models라는 모듈의 Model 클래스를 상속 받는다는 뜻이다.

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# 최종 테이블 이름은 "앱이름 _모델클래스이름" 으로 합성하여 만듦
