from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'message',
        'date',
        'year',
    )

    ordering = ('date',)


admin.site.register(Contact, ContactAdmin)
