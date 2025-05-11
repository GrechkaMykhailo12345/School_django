import os
import django

from school.models import Subject, Teacher, Classroom, Student

subject = Subject(name="Інформатика")
teacher = Teacher(first_name="Дмитро", last_name="Михайлович")
classroom = Classroom(name="9-Б")
student = Student(first_name="Михайло", last_name="Гречка")

subject.save()
teacher.save()
classroom.save()
student.save()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "School_django.settings")
django.setup()