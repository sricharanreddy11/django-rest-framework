from faker import Faker
from random import randint, random
from core.models import (
    Student,
    Department,
)

Faker = Faker()


def seed_db(n: int):
    for _ in range(n):
        student_id = 'STU-'+str(randint(1, 180))
        student_name = Faker.name()
        student_age = randint(16, 22)
        student_email = Faker.email()
        cgpa = randint(6, 10)
        address = Faker.address()
        department = Department.objects.all()[randint(0, 5)]
        student = Student(student_id=student_id, student_name=student_name, student_age=student_age, student_email=student_email, cgpa=cgpa, address=address, department=department)
        student.save()


seed_db(10)

