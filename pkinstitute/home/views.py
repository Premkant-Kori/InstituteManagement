from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home/home.html', {'nav': 'home'})

#TODO check chat-gpt and sublime