from django import forms
from student_app.models import Teacher
from student_app.forms import Teacher
import datetime

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['prenom','nom', 'email', 'matiere','date_naissance']
        widgets = {
        'prenom': forms.TextInput(attrs={
            'id':'teacher-prenom',
            'placeholder':'Prenom',
            'required': True
            }),
        'nom': forms.TextInput(attrs={
            'id':'teacher-nom',
            'placeholder':'Nom',
            'required': True
            }),
        'email': forms.EmailInput(attrs={
            'id':'teacher-email',
            'placeholder':'Email',
            'required': True
            }),
        'matiere': forms.TextInput(attrs={
            'id':'teacher-matiere',
            'placeholder':'Matiere',
            'required': True
            }),
        'date_naissance': forms.DateInput(attrs={
            'id':'teacher-date_naissance',
            'placeholder':'Date de Naissance',
            'required': True
            })
        }