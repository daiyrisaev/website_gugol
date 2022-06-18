from django import forms

from apps.gugols.models import SignIn, Category


class UserSendForm(forms.Form):
    name = forms.CharField(required=True, max_length=100)
    email = forms.EmailField(required=False)
    message = forms.CharField(required=True, max_length=100)


class SignInForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"})
    )

    class Meta:
        model = SignIn
        fields = ["category", "name", "mobile", "message", "date", "time"]
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control"
            }),
            "mobile": forms.TextInput(attrs={
                "class": "form-control"
            }),
            "message": forms.TextInput(attrs={
                "class": "form-control"
            }),
            "date": forms.DateInput(
                format="%d%m%Y",
                attrs={
                    "type": "date",
                    "class": "form-control"
                }
            ),
            "time": forms.TimeInput(
                format="%d%m%Y",
                attrs={
                    "type": "time",
                    "class": "form-control"
                }
            )
        }

