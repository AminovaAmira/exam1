from django.contrib import admin
from .models import AAExam
from django.contrib.auth.models import User

class AAExamAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'exam_date', 'is_public')
    list_filter = ('is_public', 'created_at')
    search_fields = ('name', 'users__email')
    filter_horizontal = ('users',)
    date_hierarchy = 'exam_date'

admin.site.register(AAExam, AAExamAdmin)
