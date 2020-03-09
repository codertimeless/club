from django.db import models


class Unit(models.Model):
    name = models.CharField(verbose_name="单位名称", max_length=20)
    phone = models.CharField(max_length=11, verbose_name="单位联系电话")

    def __str__(self):
        return self.name
