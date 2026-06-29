# forms.py - UPDATE with proper attributes
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            "placeholder": "Your full name",
            "class": "form-control",
            "id": "name"
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "placeholder": "Your e-mail",
            "class": "form-control",
            "id": "email"
        })
    )
    phone = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={
            "placeholder": "Phone number",
            "class": "form-control",
            "id": "phone"
        })
    )
    company = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            "placeholder": "Company name",
            "class": "form-control",
            "id": "company"
        })
    )
    subject = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={
            "placeholder": "Subject",
            "class": "form-control",
            "id": "subject"
        })
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            "placeholder": "Your message",
            "class": "form-control",
            "id": "message",
            "rows": 5
        })
    )