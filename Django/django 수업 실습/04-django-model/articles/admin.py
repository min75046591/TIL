from django.contrib import admin
from .models import Article

# Register your models here.
# admin 사이트에 등록한다. Article 클래스를
admin.site.register(Article)