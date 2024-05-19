from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import House, Comment

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=15)

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'password1', 'password2']

class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = ['name', 'address', 'landmark', 'city', 'state', 'price', 'number_of_bedrooms','picture']

class HouseFilterForm(forms.Form):
    name = forms.CharField(required=False)
    city = forms.CharField(required=False)
    state = forms.CharField(required=False)
    min_price = forms.DecimalField(required=False, max_digits=10, decimal_places=2)
    max_price = forms.DecimalField(required=False, max_digits=10, decimal_places=2)
    min_bedrooms = forms.IntegerField(required=False)
    max_bedrooms = forms.IntegerField(required=False)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
