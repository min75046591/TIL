from django.db import models
from django.contrib.auth.models import AbstractUser


# AbstractUser는 Django에서 기본 제공하는 User 모델을 상속받아 커스텀 User 모델을 만들 수 있게 해주는 클래스입니다.
class User(AbstractUser):
    pass
