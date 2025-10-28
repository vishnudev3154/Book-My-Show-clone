from django.shortcuts import render

def index(request):
    return render(request,'ind.html')


def kanthara(request):
    return render(request, 'kanthara.html')