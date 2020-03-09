from django.contrib import admin

from management.models import teacher, activity, club, student, unit

admin.site.register(teacher.Teacher)
admin.site.register(activity.Activity)

admin.site.register(club.Club)
admin.site.register(student.Student)
admin.site.register(unit.Unit)
