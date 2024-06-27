from django import forms
from .models import *

class rsvp_orderForm(forms.ModelForm):
    class Meta:
        model = rsvp_order
        fields = ['name', 'email', 'phone', 'event_details']

class FormDataForm(forms.Form):
    class Meta:
        model = custome
        fields = ('ph' ,'email','billing_name', 'gstnumber', 'billing_address',
                                 'you', 'Name', 'Instagrame_id', 'fathter_name', 'mother_name', 'grandfathter_name', 
                                 'grandmother_name', 'image', 'Spouse', 'SpouseName', 'SpouseInstagrame_id', 
                                 'Spousefathter_name', 'Spousemother_name', 'Spousegrandfathter_name',
                                 'Spousegrandmother_name', 'Spouseimage', 'Event_name', 'date_field', 'time_field',
                                 'venue', 'Description')
        
class ProductFilterForm(forms.Form):
    #name = forms.CharField(required=False)
    #category = forms.CharField(required=False)
    min_price = forms.DecimalField(required=False, min_value=0)
    max_price = forms.DecimalField(required=False, min_value=0)
    style = forms.CharField()
    Theme = forms.CharField()
    size = forms.CharField()
    Format = forms.CharField()

from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=10)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)



from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone_number', 'image']
class CollectionForm(forms.ModelForm):
    class Meta:
        model = Product  # Change this to match your Product model
        fields = ['image', 'category', 'product_name', 'price', 'Description', 'status']
        widgets = {'category': forms.Select(choices=[(cat.name, cat.name) for cat in sub_category.objects.all()])}

from django import forms

class ProductSearchForm(forms.Form):
    search_query = forms.CharField(max_length=100, required=False)



class RegistrationForm(forms.Form):
    
    phone_number = forms.CharField(max_length=15, required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'user.userprofile.phone_number', 'password1', 'password2']
