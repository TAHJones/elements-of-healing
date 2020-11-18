from django.db import models
from datetime import datetime


class BookAppointment(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=50, null=False, blank=False)
    message = models.TextField(max_length=300, null=True, blank=True)
    date = models.CharField(max_length=10, null=False, blank=False)
    time = models.CharField(max_length=10, null=False, blank=False)

    def __str__(self):
        return self.name


class AppointmentsCalendar(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=50, null=False, blank=False)
    message = models.TextField(max_length=300, null=True, blank=True)
    date = models.DateTimeField(default=datetime.today)
    time = models.CharField(max_length=10, null=False, blank=False)

    def __str__(self):
        return self.name
