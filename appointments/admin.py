from django.contrib import admin
from .models import AppointmentsCalendar


class AppointmentAdmin(admin.ModelAdmin):
    list_display = (
        'user_profile',
        'user',
        'email',
        'message',
        'date',
    )

    fields = (
        'user_profile',
        'user',
        'name',
        'email',
        'message',
        'date',
        'date_str',
        'time',
        'confirmed',
        'eventId',
    )

    ordering = ('date',)


admin.site.register(AppointmentsCalendar, AppointmentAdmin)
