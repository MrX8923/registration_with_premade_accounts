from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *


class MyMailField(forms.EmailField):
    def __init__(self, **kwargs):
        super(MyMailField, self).__init__(**kwargs)
        self.required = True


class SingUpForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = ('username', 'first_name', 'last_name', 'age', 'email', 'password1', 'password2', 'bio', 'age_18')
        field_classes = {'email': MyMailField}

        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'arkasha2000'}),
            'email': forms.EmailInput(attrs={'placeholder': 'arkasha@mail.ru'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Аркадий'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Аркадьев'}),
            'bio': forms.Textarea(attrs={'placeholder': 'Расскажите о себе'}),
            'age': forms.NumberInput(attrs={'placeholder': '18+'}),
        }

    def __init__(self, *args, **kwargs):
        super(SingUpForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'autocomplete': 'new-password',
                                                                     'placeholder': '********'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'autocomplete': 'new-password',
                                                                     'placeholder': '********'})
