from django.db import models

from club.models.club import Club

types = [
    ("大型活动", "Large-scale"),
    ("常规活动", "Regular"),
    ("素拓活动", "Extension")
]


class Activity(models.Model):
    main_club = models.ForeignKey(Club, verbose_name="主办社团")
    cooperated_club = models.ForeignKey(Club, verbose_name="协办社团")

    date = models.DateTimeField(verbose_name="活动时间")
    activity_type = models.CharField(choices=types, verbose_name="活动类型")
    activity_people_count = models.IntegerField(verbose_name="活动参与人数")
    venue = models.CharField(verbose_name="活动地点")
    score = models.IntegerField(verbose_name="活动分数")
