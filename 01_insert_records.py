from math import radians
import os
from unicodedata import name

from numpy import insert 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelExam2.settings')
from django import setup
setup()

from ModelApp2.models import Students, TestResults, Tests, Classes
from random import randint

class_names = ['Class' + c for c in 'ABCDEFGHIJ' ]
student_names = ['Student' + c for c in 'ABCDEFGHIJ']
test_names = ['数学', '英語', '国語']

insert_tests = []
for test_name in test_names:
    test = Tests(
        name=test_name
    )
    test.save()
    insert_tests.append(test)

for class_name in class_names:
    insert_class = Classes(
        name = class_name
    )
    insert_class.save()
    for student_name in student_names:
        name = class_name + ' ' + student_name
        student = Students(
            name = name,
            class_fk = insert_class,
            grade = 1
        )
        student.save()
        for inserted_test in insert_tests:
            tests_result = TestResults(
                student = student,
                test = inserted_test,
                score = randint(50,100)
            )