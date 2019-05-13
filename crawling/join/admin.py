#파이썬 어드민에 모델 등록
from django.contrib import admin
from .models import * # 모든 모델을 불러옵니다.
admin.site.register(join)
admin.site.register(choice)