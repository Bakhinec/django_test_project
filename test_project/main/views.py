# from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    data = {
        'title': 'Главная страница',
        #'values': [True, 'Hello', 123],
        #'obj': {
            #'car': 'BMW',
            #'age': 18,
            #'hobby': 'Football'

        #}
    }
    return render(request, 'main/index.html',data)

def about(request):
    return render(request, 'main/about.html')
