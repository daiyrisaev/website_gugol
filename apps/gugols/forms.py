from django import forms

from apps.gugols.models import SignIn


class UserSendForm(forms.Form):
    name = forms.CharField(required=True,max_length=100)
    email = forms.EmailField(required=False)
    message = forms.CharField(required=True, max_length=100)


class SignInForm(forms.ModelForm):
    class Meta:
        model = SignIn
        fields = ['first_name', 'last_name', 'date', 'phone', 'message']


# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ['name','email','message']
#

