from django.db import models

# Create your models here.

class Record(models.Model):
    first_name = models.CharField(max_length=50)
    last_name =  models.CharField(max_length=50)
    email =  models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    address =  models.CharField(max_length=100)
    city =  models.CharField(max_length=50)
    state =  models.CharField(max_length=50)
    pincode =  models.CharField(max_length=20)


# class SignUpForm(UserCreationForm):
#     first_name = models.CharField(label="First Name", max_length=100)
#     last_name = models.CharField(label="Last Name", max_length=100)
#     email = models.CharField(label="Email",max_length=100)
#     address = models.CharField(label="Address")
#     city = models.CharField(label="City", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':''}))
#     state = models.CharField(label="State", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':''}))
#     pincode = models.IntegerField(label="Pincode", widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':''}))
	
    def __str__(self):
        return (f"{self.first_name} {self.last_name}")
    