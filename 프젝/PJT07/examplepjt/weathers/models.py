from django.db import models

# Create your models here.

class Weather(models.Model):
    dt_txt = models.DateTimeField()     # 관측 시간
    temp = models.FloatField()          # 온도 (기본값: 캘빈온도)
    feels_like = models.FloatField()    # 체감 온도(기본값: 캘빈온도)
    