from django.db import models

from club.models.teacher import People


class Student(People):
    affiliated_college = models.ForeignKey(Unit, verbose_name="所属学院")


