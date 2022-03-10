from django import forms
from tempus_dominus.widgets import DatePicker
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, UserChangeForm
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from .models import Post
import datetime

class SignUpForm(UserCreationForm):
   password1 =forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
   password2 =forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
   class Meta:
      model =User
      fields =['first_name','last_name','username','email']
      labels ={'email':'Email-ID'}
      widgets ={
      'first_name':forms.TextInput(attrs={'class':'form-control'}),
      'last_name':forms.TextInput(attrs={'class':'form-control'}),
      'username':forms.TextInput(attrs={'class':'form-control'}),
      'email':forms.EmailInput(attrs={'class':'form-control'}),
      }

class LoginUserForm(AuthenticationForm):
  username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
  password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','strip':False,
  'autocomplete':'current-password'}))


class NewPostForm(forms.ModelForm):
  class Meta:
    model =Post
    current_date =datetime.datetime.today().date()
    fields = ['text','created_at']
    widgets ={'text':forms.Textarea(attrs={'class':'form-control'}),
    'created_at':DatePicker(options={'minDate': '2022-01-01','maxDate': str(current_date),}),
    }
    def clean(self):
      cleaned_data = self.cleaned_data
      end_time = cleaned_data.get('updated_at') # this is not None if user left the <input/> empty
      # ... do stuff with data

      if not end_time:
          cleaned_data['updated_at'] = None

      return cleaned_data

class UpdatePostForm(forms.ModelForm):
  class Meta:
    model =Post
    current_date =datetime.datetime.today().date()
    fields = ['text','updated_at']
    widgets ={'text':forms.Textarea(attrs={'class':'form-control'}),
    'updated_at':DatePicker(options={'minDate': '2022-01-01','maxDate': str(current_date),}),
    }
    
class AdminProfileForm(UserChangeForm):
  password = None
  class Meta:
    model =User
    fields = '__all__'
    widgets ={
      'first_name':forms.TextInput(attrs={'class':'form-control'}),
      'last_name':forms.TextInput(attrs={'class':'form-control'}),
      'groups':forms.SelectMultiple(attrs={'class':'form-control'}),
      'user_permissions':forms.SelectMultiple(attrs={'class':'form-control'}),
      'password':forms.TextInput(attrs={'class':'form-control'}),
      'email':forms.EmailInput(attrs={'class':'form-control'}),
      'username':forms.TextInput(attrs={'class':'form-control'}),
      'date_joined':forms.DateTimeInput(attrs={'class':'form-control'}),
      'last_login':forms.TextInput(attrs={'class':'form-control'}),
      'is_active':forms.CheckboxInput(attrs={'class':'form-check-input'}),
      'is_staff':forms.CheckboxInput(attrs={'class':'form-check-input'}),
      'is_superuser':forms.CheckboxInput(attrs={'class':'form-check-input'}),

    }

class UserProfileForm(AdminProfileForm):
  password = None
  class Meta(AdminProfileForm.Meta):
    fields =['first_name','last_name','username','email','date_joined','last_login']
