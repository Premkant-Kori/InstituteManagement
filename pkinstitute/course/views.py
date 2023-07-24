from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'course/all_courses.html')
