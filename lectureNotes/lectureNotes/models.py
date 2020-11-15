from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Course(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.TextField()

class Note(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField()
    noteText = models.TextField()
    link = models.TextField()

class Permission(models.Model):
	note = models.ForeignKey(Note, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
