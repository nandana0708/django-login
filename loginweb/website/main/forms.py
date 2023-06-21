from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record

# class ProfilePicForm(forms.ModelForm):
#     profile_image = forms.ImageField(label='Profile Picture')

#     class Meta:
#         model = Record
#         fields = ('profile_image')
	 
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label="First Name", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':''}))
    last_name = forms.CharField(label="Last Name", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':''}))
    email = forms.EmailField(label="Email", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':''}))
    address = forms.CharField(label="Address", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':''}))
    city = forms.CharField(label="City", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':''}))
    state = forms.CharField(label="State", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':''}))
    pincode = forms.IntegerField(label="Pincode", widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':''}))
	
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'address', 'city', 'state', 'pincode')
	
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	