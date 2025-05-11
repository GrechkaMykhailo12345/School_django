from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    subjects = models.ManyToManyField(Subject, related_name='teachers')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Classroom(models.Model):
    name = models.CharField(max_length=20, unique=True)
    grade = models.IntegerField()
    head_teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, related_name='leading_classes')

    def __str__(self):
        return f"{self.grade}-{self.name}"

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    classroom = models.ForeignKey(Classroom, on_delete=models.SET_NULL, null=True, related_name='students')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
