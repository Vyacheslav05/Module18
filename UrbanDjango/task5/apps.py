from django.apps import AppConfig


class Task5Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'task5'

from django import forms
from django.core.validators import MinLengthValidator, MaxLengthValidator, MaxValueValidator


class UserRegisterForm(forms.Form):
    username = forms.CharField(
        label="Введите логин",
        max_length=30,
        validators=[MaxLengthValidator(30)]
    )
    password = forms.CharField(
        label="Введите пароль",
        widget=forms.PasswordInput,
        validators=[MinLengthValidator(8)]
    )
    repeat_password = forms.CharField(
        label="Повторите пароль",
        widget=forms.PasswordInput,
        validators=[MinLengthValidator(8)]
    )
    age = forms.IntegerField(
        label="Введите свой возраст",
        validators=[MaxValueValidator(3)]
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        repeat_password = cleaned_data.get("repeat_password")

        if password and repeat_password and password != repeat_password:
            raise forms.ValidationError("Пароли не совпадают")

        return cleaned_data