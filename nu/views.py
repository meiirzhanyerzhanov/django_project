from django.shortcuts import render
from .models import Teacher
from .models import Course
from .models import Student

def index(request):
    courses = Course.objects.all()
    return render(request, 'nu/index_extend.html', {'courses': courses})