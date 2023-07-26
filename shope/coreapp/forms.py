from django import forms
from phonenumber_field.formfields import PhoneNumberField


class ContactForm(forms.Form):
    """
    Класс формы для валидации данных от пользователя
    """
    phone_number = forms.CharField(required=True, max_length=30)
    email = forms.CharField(required=False, max_length=40)
    name = forms.CharField(required=True, max_length=25)
