from django.db import models
from datetime import datetime
from django.urls import reverse


class AppointmentsCalendar(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=50, null=False, blank=False)
    message = models.TextField(max_length=300, null=True, blank=True)
    date = models.DateTimeField(default=datetime.today)
    date_str = models.CharField(max_length=10, null=False, blank=False)
    time = models.CharField(max_length=10, null=False, blank=False)

    def __str__(self):
        return self.name

    @property
    def get_html_url(self):
        url = reverse('appointment_details', args=(self.id,))
        return f'<a href="{url}">{self.name}</a>'
