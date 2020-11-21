from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from bincom.models import Polling_unit, State, Ward, Lga

# class SignUpForm(UserCreationForm):
#     first_name = forms.CharField(max_length=100, help_text='Last Name')
#     last_name = forms.CharField(max_length=100, help_text='Last Name')
#     email = forms.EmailField(max_length=150, help_text='Email')


#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'last_name',
# 'email', 'password1', 'password2',)




class SignUpForm(UserCreationForm):
    name = forms.CharField(max_length=30,  required=False, help_text='Optional.')
    username= forms.CharField(max_length=30,required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
  

    class Meta:
        model = User
        fields = ('username', 'name', 'email',
                  'password1', 'password2')

# class NewProfileForm(forms.ModelForm):
#     class Meta:
#         model = User
#         exclude = ['user','bio'] 
#         widgets = {
#             'tags': forms.CheckboxSelectMultiple(),
#         }




# class TimeForm(forms.ModelForm):
#     # submit = SubmitField('Add Time') 
#         model = Timeslot
#         fields = ['date','start_time','end_time']       
        
        



# class BookingForm(forms.ModelForm):
#     class Meta:
#         model = Booking
#         exclude = ['user', 'profile']

class PollingUnitForm(forms.ModelForm):


    class Meta:
        model = Polling_unit
        # fields=['polling_unit_name', 'party_score', 'part_choices']
        exclude=['user','lat','lng','date_entered','party_id','polling_user','user_ip_address']
       
    
  

class LgaForm(forms.ModelForm):


    class Meta:
        model = Lga
        # fields=['polling_unit_name', 'party_score', 'part_choices']
        exclude=['ward_id','entered_by_user','date_entered']
       



class WardForm(forms.ModelForm):


    class Meta:
        model = Ward
        # fields=['polling_unit_name', 'party_score', 'part_choices']
        exclude=['ward_id','user_ip_address','date_entered','polling_unit_id', 'user']
       


class StateForm(forms.ModelForm):


    class Meta:
        model = State
        # fields=['polling_unit_name', 'party_score', 'part_choices']
        exclude=['state_id']
       
            