from django.shortcuts import render

# Create your views here.
active = {
    'nav': 'active'
}


def home(request):
    return render(request, 'base.html', {'nav': 'home'})


def course(request):
    return render(request, 'course/all_courses.html', {'nav': 'courses'})
