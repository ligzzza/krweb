from django.db import models
from django.contrib.auth.models import User


class geeхам(models.Model):
    # Поле для названия экзамена
    name = models.CharField(max_length=255, verbose_name="Название экзамена")
    # Дата создания записи
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    # Дата проведения экзамена
    exam_date = models.DateField(verbose_name="Дата проведения экзамена")
    # Поле для добавления изображения (например, задание в виде картинки)
    image = models.ImageField(upload_to='exam_images/', null=True, blank=True, verbose_name="Изображение задания")
    # Многие ко многим: пользователи, которые пишут экзамен
    participants = models.ManyToManyField(User, related_name='exams', verbose_name="Пользователи")
    # Поле для публикации записи
    is_public = models.BooleanField(default=False, verbose_name="Опубликовано")

    def __str__(self):
        return self.name