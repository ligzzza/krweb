

from django.shortcuts import render
from .models import geeхам  # ваша модель

def exam(request):
    # Получаем все опубликованные записи модели geeхам
    exams = geeхам.objects.filter(is_public=True)
    context = {
        'exams': exams,
        'fio': 'Ваше ФИО',              # замените на ваше ФИО
        'group_number': 'Номер группы'  # замените на номер вашей группы
    }
    return render(request, 'geexam.html', context)
