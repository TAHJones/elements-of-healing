from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput
from django import forms
from .models import BookAppointment


class AppointmentDatePickerInput(DatePickerInput):
    template_name = 'appointments/date-picker.html'


class AppointmentTimePickerInput(TimePickerInput):
    template_name = 'appointments/time-picker.html'


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = BookAppointment
        fields = ['name', 'email', 'message', 'date', 'time']
        widgets = {
            'date': AppointmentDatePickerInput(),
            'time': AppointmentTimePickerInput(),
        }

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Full Name',
            'email': 'Email Address',
            'message': 'Enter Message',
        }

        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            for key, value in placeholders.items():
                if field == key:
                    self.fields[field].widget.attrs['placeholder'] = value
                    self.fields[field].widget.attrs['class'] = 'form-style-input'
