from django import forms


class UserSendForm(forms.Form):
    name = forms.CharField(required=True,max_length=100)
    email = forms.EmailField(required=False)
    message = forms.CharField(required=True, max_length=100)