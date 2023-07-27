from django.shortcuts import render
from course.models import Course

# Create your views here.
active = {
    'nav': 'active'
}





def course(request):
    course_list = Course.objects.all()
    data = {
        'nav': 'courses',
        'course_list': course_list
    }
    return render(request, 'course/all_courses.html', data)
