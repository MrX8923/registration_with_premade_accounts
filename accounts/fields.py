from django import forms

from .validators import *


class MyMailField(forms.EmailField):
    def __init__(self, **kwargs):
        super(MyMailField, self).__init__(**kwargs)
        self.required = True


class MyAgeField(forms.IntegerField):
    def __init__(self, **kwargs):
        super(MyAgeField, self).__init__(**kwargs)
        self.required = True
        self.validators.append(age_validator)


class MyAge18Field(forms.BooleanField):
    def __init__(self, **kwargs):
        super(MyAge18Field, self).__init__(**kwargs)
        self.required = True
