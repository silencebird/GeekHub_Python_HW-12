from django import forms

from geekhub.models import Student
from geekhub.models import Course


class PostForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('first_name', 'second_name', 'email')
