from django import forms
from allauth.account.forms import SignupForm, LoginForm
from .models import CustomUser, UserProfile

class CustomSignupForm(SignupForm):
    field_of_activity = forms.ChoiceField(choices=[
        ('IT', 'Информационные технологии'),
        ('Маркетинг', 'Маркетинг'),
        ('Производство', 'Производство'),
    ], label='Сфера деятельности')
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ['field_of_activity', 'email', 'password1', 'password2',]

class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        self.fields['login'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'form-control'})
        
    def get_user(self):
        return self.user
    
class UserProfileForm(forms.ModelForm):
    birth_date = forms.DateField(widget=forms.TextInput(attrs={'id': 'id_birth_date'}), required=False)

    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_picture', 'gender', 'birth_date']
