from django.db import models
from django.conf import settings

categories = (
    # ('저장될 값', '화면에 보여질 값')
    ('programming', '프로그래밍'),
    ('essay', '에세이'),
    ('novel', '소설'),
    ('science', '과학'),
)

class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    page_count = models.IntegerField()

    # choices를 사용하여 선택지를 제공, choices에 지정된 값은 데이터베이스에 저장됩니다.
    # categories 에 존재하지 않는 값은 저장할 수 없도록 설정합니다.
    category = models.CharField(max_length=50, choices=categories)

    price = models.DecimalField(max_digits=10, decimal_places=2)  # 10자리 정수, 소수점 2자리

    # ISBN 필드를 추가합니다. ISBN은 국제 표준 도서 번호, 조회 연습을 위해 가상의 형태로 구성합니다. EX) ABC123123123 OR 123123123ABC -> 12자리
    isbn = models.CharField(max_length=12)
    # ForeignKey를 사용하여 User 모델과 연결합니다.
    # on_delete=models.CASCADE는 author 모델이 삭제되면 연결된 Book 모델도 삭제되도록 설정합니다.
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    review_text = models.TextField()
    reviewer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)