from django.db import models

from management.models.People import People
from .unit import Unit


class Student(People):
    affiliated_college = models.ForeignKey(Unit, verbose_name="所属学院", on_delete=models.DO_NOTHING)


