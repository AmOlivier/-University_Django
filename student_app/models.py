from django.db import models

# Create your models here.
class Student(models.Model):
    prenom = models.CharField(max_length=20)
    nom = models.CharField(max_length=20)
    date_naissance = models.DateField()
    
    def __repr__(self):
        return"<Topic {}>".format(self.nom)

    def __str__(self):
        return self.nom


class Note(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	matiere = models.CharField(max_length=20)
	note = models.IntegerField(default=0)
	coefficient = models.IntegerField(default=0)


	def __str__(self):
		return self.matiere

class Teacher(models.Model):
    prenom = models.CharField(max_length=20)
    nom = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    matiere = models.CharField(max_length=20)
    date_naissance = models.DateField()

    def __repr__(self):
        return"<Topic {}>".format(self.nom)

    def __str__(self):
        return self.nom

    


