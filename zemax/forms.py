from django import forms
from .models import House
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail


class NewHouse(forms.ModelForm):
    house_image = forms.ImageField(required=False)
    image2 = forms.ImageField(required=False)
    image3 = forms.ImageField(required=False)
    image4 = forms.ImageField(required=False)
    image5 = forms.ImageField(required=False)
    image6 = forms.ImageField(required=False)
    image7 = forms.ImageField(required=False)
    image8 = forms.ImageField(required=False)
    image9 = forms.ImageField(required=False)
    image10 = forms.ImageField(required=False)
    image11 = forms.ImageField(required=False)
    image12 = forms.ImageField(required=False)
    image13 = forms.ImageField(required=False)
    image14 = forms.ImageField(required=False)
    image15 = forms.ImageField(required=False)
    image16 = forms.ImageField(required=False)
    image17 = forms.ImageField(required=False)
    address = forms.CharField(max_length=255)
    price = forms.IntegerField()
    bedrooms = forms.IntegerField()
    bathrooms = forms.FloatField()
    square_feet = forms.IntegerField()
    description = forms.CharField(widget=forms.Textarea)
    year = forms.IntegerField()
    agent = forms.CharField(max_length=255)
    contact = forms.EmailField(max_length=255)
    sold = forms.BooleanField(label='Already Sold? ')

    class Meta:
        model = House
        fields = ['house_image', 'image2', 'image3', 'image4', 'image5', 'image6', 'image7', 'image8', 'image9', 'image10',
                  'image11', 'image12', 'image13', 'image14', 'image15', 'image16', 'image17', 'address', 'price',
                  'bedrooms', 'bathrooms', 'square_feet', 'description', 'year', 'agent', 'contact', 'sold']


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class SendEmailForm(forms.Form):
    subject = forms.CharField(max_length=255)
    email_body = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    recipient = forms.EmailField()




