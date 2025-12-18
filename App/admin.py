from django.contrib import admin
from .models import StudentInfo, TimeTable, Income
# Register your models here.

admin.site.register(StudentInfo)
admin.site.register(TimeTable)
admin.site.register(Income)