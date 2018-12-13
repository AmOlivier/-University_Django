import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_project.settings')
import django
django.setup()


import random
from faker import Faker
from student_app.models import Student, Note, Teacher


fakegen = Faker()
def generate_matieres():
	matieres = ["Espagnol", "Philosophie", "SVT", "Sorcelerie"]
	index = random.randint(0, 3)
	return matieres[index]



def populate():
	for student in range(2):
		note = random.randint(0, 10)
		coefficient = random.randint(0, 5)
		matiere = generate_matieres()
		newStudent = Student.objects.get_or_create(nom=fakegen.last_name(), prenom=fakegen.first_name(), date_naissance=fakegen.date())
		newNote = Note.objects.get_or_create(student=newStudent[0], matiere=matiere, note=note , coefficient = coefficient)
		print(newStudent,newNote)




def populate_teacher():
	for prof in range(3):
		matiere = generate_matieres()
		newProfessor = Teacher.objects.get_or_create(nom=fakegen.last_name(), prenom=fakegen.first_name(), email=fakegen.email(), matiere=matiere, date_naissance=fakegen.date())
		print(newProfessor)



if __name__ == '__main__':
	 print('populate script...')
	 populate()
	 populate_teacher()
	 print('done populating.')