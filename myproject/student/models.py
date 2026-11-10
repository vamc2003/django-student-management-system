from django.db import models

class School(models.Model):
    school_name = models.CharField(max_length=150)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.school_name


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    course = models.CharField(max_length=100)

    school = models.ForeignKey(
    School,
    on_delete=models.CASCADE,
    related_name='students',
    null=True,
    blank=True
)
    def __str__(self):
        return self.name