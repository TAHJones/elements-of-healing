from django.contrib import admin
from .models import AppointmentsCalendar


class AppointmentAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'message',
        'date',
        'date_str',
        'time',
    )

    ordering = ('date',)


admin.site.register(AppointmentsCalendar, AppointmentAdmin)
