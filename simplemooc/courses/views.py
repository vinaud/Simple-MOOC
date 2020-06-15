from django.shortcuts import render

def courses(request):
    template_name = 'course/courses.html'
    return render(request,template_name)