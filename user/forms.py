from django import forms


class NameForm(forms.Form):
    your_name = forms.CharField(label='your_name', max_length=100)
     your_school = forms.CharField(label='your_name', max_length=100)
         your_batch = forms.CharField(label='your_name', max_length=100)
             your_age = forms.CharField(label='your_name', max_length=100)
