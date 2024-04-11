from django.shortcuts import render
from django.http import HttpResponse

# import our Ml module here

import test

# Create your views here.
 

def index(request):
   return render(request, 'index.html')

def feature(request):
    return render(request, 'feature.html')

def about(request):
   return render(request, 'about.html')

def happy(request):
    return render(request, 'happy.html')

def sad(request):
    return render(request, 'sad.html')

def angry(request):
    return render(request, 'angry.html')

def disgust(request):
    return render(request, 'disgust.html')

def fear(request):
    return render(request, 'fear.html')

def neutral(request):
    return render(request, 'neutral.html')

def surprise(request):
    return render(request, 'surprise.html')

# def emotion(request):

def check(request):
    status = request.GET.get('Onn', 'off')
    if status =='Check':
        test.model()
        return render(request, 'index.html')
        # print(status)
    else:
        # print(status)
        return render(request, 'index.html')

