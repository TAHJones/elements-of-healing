from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput
from django import forms
from .models import Appointments


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointments
        fields = ['name', 'date', 'time', 'month', 'year']
        widgets = {
            'date': DatePickerInput(),
            'time': TimePickerInput(),
            'month': MonthPickerInput(),
            'year': YearPickerInput(),
        }
