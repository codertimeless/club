from management.models.student import Student
from management.models.unit import Unit
from management.models.teacher import Teacher

from django.db import models


# TODO Examination part of club
# TODO Communicate part (include display some news)
# TODO activities of club

STATUS_OF_CLUB = [
    ("dj", "冻结"),
    ("cx", "撤销"),
    ("zc", "正常")
]

CATEGORY_OF_CLUB = [
    ("wyty", "文娱体育"),
    ("whzh", "文化综合"),
    ("gysj", "公益实践"),
    # TODO
    ("wlss", "忘了是啥"),
]


class Club(models.Model):
    # People in club
    president = models.ForeignKey(Student, on_delete=models.DO_NOTHING, verbose_name="会长", related_name="president")
    vicePresident = models.ManyToManyField(Student, verbose_name="副会长", related_name="vicePresident")
    affiliatedUnits = models.ManyToManyField(Unit, verbose_name="挂靠单位")
    guidanceTeacher = models.ManyToManyField(Teacher, verbose_name="指导老师")

    # Status of a club
    name = models.CharField(verbose_name="社团名称", max_length=15)
    club_status = models.CharField(choices=STATUS_OF_CLUB, verbose_name="社团状态", max_length=2)
    club_category = models.CharField(choices=CATEGORY_OF_CLUB, verbose_name="社团类别", max_length=4)
    create_time = models.DateField(verbose_name="成立时间")
    particular_year = models.CharField(verbose_name="运行年份", max_length=4)
    description = models.CharField(verbose_name="社团描述", max_length=50)
    purpose = models.CharField(verbose_name="社团宗旨", max_length=50)
    icon = models.ImageField(verbose_name="社团图标")

    def get_particular_year_count(self, particular_year, club):
        return Student.object.filter(particular_year=particular_year, club=club).count()

    def __str__(self):
        return self.name
