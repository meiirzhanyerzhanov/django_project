from django.contrib import admin
from .models import Teacher
from .models import Course
from .models import Student


admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Student)