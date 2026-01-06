from random import choices
from django.db import models

# Create your models here.

class StudentInfo(models.Model):
    name = models.CharField(max_length=100)
    school = models.CharField(max_length=150)
    class_name = models.CharField(max_length=20)
    contact = models.CharField(max_length=15)
    admission_date = models.DateField()
    fees = models.IntegerField(default=0)
 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class TimeTable(models.Model):
    DAY_CHOICES = [
        ('SUN', 'Sunday'),
        ('MON', 'Monday'),
        ('TUE', 'Tuesday'),
        ('WED', 'Wednesday'),
        ('THU', 'Thursday'),
        ('FRI', 'Friday'),
        ('SAT', 'Saturday'),
    ]

    day = models.CharField(max_length=3, choices=DAY_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()
    subject = models.CharField(max_length=100, blank=True)
    teacher = models.CharField(max_length=100, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.day} ({self.start_time} - {self.end_time})"

class Income(models.Model):

    REMARK = [('CASH', 'cash'),
                ('ONLINE', 'online'),
                ('CREDIT', 'credit')
    ]

    date = models.DateField()
    amount = models.IntegerField()
    remarks = models.CharField(max_length = 6, choices = REMARK)
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"{self.amount} ({self.remarks})"

