from django import forms
from.models import Student,Fees

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class FeeForm(forms.ModelForm):
    class Meta:
        model = Fees
        fields = '__all__'
