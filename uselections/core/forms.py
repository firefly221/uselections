from django.forms import ModelForm,widgets
from django import forms
from .models import Voter


class VoterForm(ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = Voter
        fields = ['name','email','password','confirm_password','state','gender','education']
        widgets = {
            'password' : forms.PasswordInput(attrs={'class':'form-control'}),
            'name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'state' : forms.Select(attrs={'class' : 'form-control'}),
            'gender' : forms.Select(attrs={'class' : 'form-control'}),
            'education' : forms.Select(attrs={'class' : 'form-control'}),
            'email' : forms.TextInput(attrs={'class' : 'form-control'})
        } 
    def clean(self):
        cleaned_data = super(VoterForm,self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError(
                "passwords don't match"
            )


