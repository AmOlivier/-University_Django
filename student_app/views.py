from django.shortcuts import render
from student_app.models import Student, Note 

# Create your views here.
def index(request):
	students = Student.objects.all().order_by('id')
	return render(request,'students/index.html', context={'students':students})

def details(request, student_id):
	student = Student.objects.get(id=student_id)
	notes = Note.objects.all().filter(student=student)
	return render(request,'students/details.html', context={'student':student, 'notes':notes})

