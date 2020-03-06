from django.db import models

from club.models.teacher import Teacher


class Unit(models.Model):
    name = models.CharField(verbose_name="单位名称")
    person_in_charge = models.ForeignKey(Teacher, verbose_name="单位负责人")
    phone = models.CharField(max_length=11, verbose_name="单位联系电话")
