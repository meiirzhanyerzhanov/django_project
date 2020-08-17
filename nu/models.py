from django.db import models


class Teacher(models.Model):
    name = models.CharField('Имя', max_length=20)
    surname = models.CharField('Фамилия', max_length=20)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField('Имя', max_length=20)
    surname = models.CharField('Фамилия', max_length=20)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField('Название', max_length=50)
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE, primary_key=True)
    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.name