from django import forms
from django.contrib.auth.models import User

class ShoeSearchForm(forms.Form):
    surface = forms.ChoiceField(choices=[
        ('road',   'Road'),
        ('trail',  'Trail'),
    ])
    foot_strike = forms.ChoiceField(choices=[
        ('midfoot', 'Midfoot'),
        ('heel',    'Heel'),
        ('forefoot','Forefoot'),
    ])
    cushioning = forms.ChoiceField(choices=[
        ('Medium', 'Medium'),
        ('Soft',   'Soft'),
        ('Plush',  'Plush'),
    ])
    pronation_support = forms.BooleanField(required=False)

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        
class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=150)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)