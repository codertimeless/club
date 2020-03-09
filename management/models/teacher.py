from django.db import models

from management.models.unit import Unit
from .People import People


class Teacher(People):
    work_unit = models.ForeignKey(Unit, verbose_name="工作单位", on_delete=models.DO_NOTHING)

