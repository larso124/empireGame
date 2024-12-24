from django import forms

class EnterName(forms.Form):
    enter_name = forms.CharField(label="Enter Empire Name", max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Type Here'}))