from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class AAExam(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название экзамена')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания записи')
    exam_date = models.DateTimeField(verbose_name='Дата проведения экзамена')
    image = models.ImageField(upload_to='exam_images/', verbose_name='Изображение задания', null=True, blank=True)
    users = models.ManyToManyField(User, verbose_name='Пользователи для экзамена')
    is_public = models.BooleanField(default=False, verbose_name='Опубликовано')

    class Meta:
        verbose_name = 'Экзамен'
        verbose_name_plural = 'Экзамены'

    def __str__(self):
        return self.name