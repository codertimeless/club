from django.db import models

from club.models.unit import Unit

gender = [
    ("Male", "男"),
    ("Female", "女"),
]


class People(models.Model):
    name = models.CharField(verbose_name="姓名")
    gender = models.CharField(verbose_name="性别", choices=gender)
    phone = models.IntegerField()


class Teacher(People):
    work_unit = models.ForeignKey(Unit, verbose_name="工作单位")
