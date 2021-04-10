from django.contrib import admin
from multichoiceq.models import Question,Choice

admin.site.register(Question)
admin.site.register(Choice)