from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
  class Meta:
    model = Student
    fields = '__all__'
    
  def __init__(self, *args, **kwargs):
    super(StudentForm, self).__init__(*args, **kwargs)
    self.fields['email'].required = False
    self.fields['hometown'].required = False
    self.fields['date_of_birth'].required = False