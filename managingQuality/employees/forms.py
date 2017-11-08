from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee

        fields = ['first_name', 'second_name', 'last_name', 'email', 'phone']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_base, provider = email.split("@")
        extension = provider.split("uoitc")
        extension = provider.split('.')
        extension = provider.split("edu")
        extension = provider.split('.')
        extension = provider.split("iq")

        if not "@uoitc.edu.iq" in email:
            raise forms.ValidationError("please enter @uoitc.edu.iq domain")
        return email
