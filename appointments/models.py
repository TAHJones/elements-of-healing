from django.db import models

# Create your models here.


# class Contact(models.Model):
#     start_date = models.CharField(max_length=50, null=False, blank=False)
#     email = models.EmailField(max_length=50, null=False, blank=False)
#     message = models.TextField(max_length=300, null=False, blank=False)


class Appointments(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    # end_date = models.DateField()
    time = models.TimeField()
    # end_time = models.TimeField()
    # start_datetime = models.DateTimeField()
    # end_datetime = models.DateTimeField()
    month = models.DateField()
    # end_month = models.DateField()
    year = models.DateField()
    # end_year = models.DateField()

    def __str__(self):
        return self.name
