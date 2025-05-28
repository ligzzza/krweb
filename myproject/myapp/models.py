from django.db import models


class User(models.Model):
    email = models.EmailField()

class geeхам(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название экзамена")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    exam_date = models.DateField(verbose_name="Дата проведения экзамена")
    image = models.ImageField(upload_to='exam_images/', null=True, blank=True, verbose_name="Изображение задания")
    participants = models.ManyToManyField(User, related_name='exams', verbose_name="Пользователи")
    is_public = models.BooleanField(default=False, verbose_name="Опубликовано")

    def __str__(self):
        return self.name