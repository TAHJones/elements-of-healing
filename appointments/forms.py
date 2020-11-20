from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput
from django import forms


class AppointmentDatePickerInput(DatePickerInput):
    template_name = 'appointments/date-picker.html'


class AppointmentTimePickerInput(TimePickerInput):
    template_name = 'appointments/time-picker.html'


class AppointmentForm(forms.Form):
    name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={"class": "form-style-input", 'placeholder': 'Full Name', 'autofocus': True})
    )
    email = forms.CharField(
        max_length=50,
        widget=forms.EmailInput(attrs={"class": "form-style-input", 'placeholder': 'Email Address'})
    )

    message = forms.CharField(
        max_length=300,
        widget= forms.Textarea(attrs={'class': 'form-style-input', 'placeholder': 'Enter Message'})
    )

    date = forms.CharField(
        max_length=10,
        widget=AppointmentDatePickerInput()
    )

    time = forms.CharField(
        max_length=10,
        widget=AppointmentTimePickerInput()
    )
