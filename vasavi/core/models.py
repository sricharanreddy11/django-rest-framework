from django.db import models


class DepartmentQuerySet(models.QuerySet):
    pass


class DepartmentManager(models.Manager):
    def get_queryset(self):
        return DepartmentQuerySet(self.model, using=self._db)


class Department(models.Model):
    department_id = models.CharField(unique=True, primary_key=True, max_length=15)
    department_name = models.CharField(max_length=100)

    objects = DepartmentManager()

    def __str__(self):
        return self.department_name

    class Meta:
        ordering = ["department_name"]


class StudentQuerySet(models.QuerySet):
    pass


class StudentManager(models.Manager):
    def get_queryset(self):
        return StudentQuerySet(self.model,using=self._db)


class Student(models.Model):
    student_id = models.CharField(max_length=100)
    student_name = models.CharField(max_length=100)
    student_age = models.IntegerField(default=18)
    student_email = models.EmailField(unique=True)
    cgpa = models.FloatField(default=0.0)
    address = models.TextField()
    date_of_joining = models.DateTimeField(auto_now_add=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='students')

    objects = StudentManager()

    def __str__(self):
        return self.student_name

    class Meta:
        ordering = ["student_id"]
