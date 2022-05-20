from django import forms




class UserSendForm(forms.Form):
    name = forms.CharField(required=True,max_length=100)
    email = forms.EmailField(required=False)
    message = forms.CharField(required=True, max_length=100)

#
# class SignInForm(forms.ModelForm):
#     category = forms.ModelChoiceField(queryset=Category.objects.filter(),
#                                           widget=forms.Select(attrs={'class':'form-control'}))
#
#     class Meta:
#         model = SignIn
#         fields = ['regular_tour',  'mobile', 'notice']




# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ['name','email','message']
#

