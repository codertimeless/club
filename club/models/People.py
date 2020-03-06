from django.db import models

from club.models.unit import Unit

gender = [
    ("男", "Male"),
    ("女", "Female"),
]


class People(models.Model):
    name = models.CharField(verbose_name="姓名")
    gender = models.CharField(verbose_name="性别", choices=gender)
    phone = models.CharField(max_length=11)
