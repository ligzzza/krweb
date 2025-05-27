from django.http import HttpResponse

def home(request):
    return HttpResponse("Привет, мир! Это мой первый Django-сайт!")
