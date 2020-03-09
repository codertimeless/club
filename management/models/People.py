from django.db import models

gender = [
    ("男", "Male"),
    ("女", "Female"),
]


class People(models.Model):
    name = models.CharField(verbose_name="姓名", max_length=10)
    gender = models.CharField(verbose_name="性别", choices=gender, max_length=6)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
