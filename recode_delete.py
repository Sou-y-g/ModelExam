import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelExam2.settings')
from django import setup
setup()

from ModelApp2.models import Students, TestResults, Tests, Classes

Students.objects.all().delete()
Tests.objects.all().delete()
Classes.objects.all().delete()
TestResults.objects.all().delete()