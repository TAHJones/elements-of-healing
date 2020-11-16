from django.db import models


class BookAppointment(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=50, null=False, blank=False)
    message = models.TextField(max_length=300, null=True, blank=True)
    date = models.CharField(max_length=10, null=False, blank=False)
    time = models.CharField(max_length=10, null=False, blank=False)

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
