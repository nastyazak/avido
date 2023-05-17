from django.forms import ModelForm
from django import forms
from .models import *


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = {'username', 'first_name', 'last_name', 'patronymic', 'patronymic', 'email', 'phone',
                  'convenient_time'}


class AnnouncementForm(ModelForm):
    class Meta:
        model = Announcement
        fields = {'name_ad', 'category', 'city', 'description_ad', 'price', 'user', 'number_views',
                  'image'}


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = {'name_cat', 'code', 'parent'}


class CitiesForm(ModelForm):
    class Meta:
        model = Cities
        fields = {'name_city', 'region'}


class RegionForm(ModelForm):
    class Meta:
        model = Region
        fields = {'name_reg'}


class ModerationAdForm(ModelForm):
    class Meta:
        model = ModerationAd
        fields = {'date_moder', 'ad', 'user', 'publication', 'reason'}


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        # проверка введенных данных
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError(f'Пользователь {username} не найден')
        user = User.objects.filter(username=username).first()
        if user:
            if not user.check_password(password):
                raise forms.ValidationError('Неверный пароль')
        return self.cleaned_data

    class Meta:
        model = User
        fields = {'username', 'password'}


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField(required=True)

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Данный email занят')
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(f'Пользователь с именем {username} уже зарегистрирован')
        return username

    def clean(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError('Пароли не совпадают')
        return self.cleaned_data

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'patronymic', 'email', 'phone',
                  'convenient_time', 'password', 'confirm_password']
