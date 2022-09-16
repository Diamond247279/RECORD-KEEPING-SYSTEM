from django.forms import ModelForm
from student.models import Student


class StudentForm(ModelForm):
    class Meta:
        model = Student
        exclude = ['department']
