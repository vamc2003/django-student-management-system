from django import forms
from .models import Student

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student

        fields = [
            'name',
            'age',
            'email',
            'course',
            'school'
        ]
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=150)
    message = forms.CharField(
        widget=forms.Textarea
    )