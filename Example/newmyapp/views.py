from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def data(request):
    return HttpResponse("<h1>Страница с данными проекта Django</h1>")

def test(request):
    return HttpResponse("<h1>Это тестовая страница на Django</h1>")
