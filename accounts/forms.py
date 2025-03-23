from django import forms
from .models import MyUser

class CreateUserForm(forms.ModelForm):
    """Form for creating a new user with an email field."""
    username = forms.CharField(max_length=256)
    password1 = forms.CharField(label='password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirm Password',widget=forms.PasswordInput)
    class Meta:
        """Meta options for the CreateUserForm."""
        model = MyUser
        fields = ['username','password1','password2',"role"]
        widgets = {
            "role":forms.Select(attrs={'class':"form-control w-100"})
        }
    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if(password1 == password2 and password1 and password2):
            user =super(CreateUserForm,self).save(commit=False)
            user.set_password(self.cleaned_data.get('password1'))
            user.save()
            return super(CreateUserForm,self).clean()
        else:
            raise forms.ValidationError({"password2":"passwords don't match","password1":"passwords don't match"})
class UserUpdateForm(forms.ModelForm):
    """Form for updating existing user information."""
    class Meta:
        """Meta options for the UserUpdateForm."""
        model = MyUser
        fields = [
            'username',
            'role',
        ]