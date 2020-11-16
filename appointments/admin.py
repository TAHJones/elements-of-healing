from django.contrib import admin
from .models import BookAppointment


class AppointmentAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'message',
        'date',
        'time',
    )

    ordering = ('date',)


admin.site.register(BookAppointment, AppointmentAdmin)
