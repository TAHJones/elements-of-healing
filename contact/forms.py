from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=50, widget= forms.TextInput(attrs={'class':'form-style-input','placeholder':'Full Name'}))
    email = forms.CharField(max_length=50, widget= forms.EmailInput(attrs={'class':'form-style-input', 'placeholder':'Email Address'}))
    message = forms.CharField(max_length=300, widget= forms.Textarea(attrs={'class':'form-style-input','placeholder':'Enter Message'}))
