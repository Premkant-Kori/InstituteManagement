from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def registration_page(request):
    return render(request, 'signup.html')

def login_page(request):
    return render(request, 'login.html')

def logout(request):
    pass