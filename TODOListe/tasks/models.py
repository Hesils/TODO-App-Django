from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

class Task(models.Model):
    name = models.CharField(max_length=75)
    description = models.TextField()
    categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    

class Categorie(models.Model):
    name = models.CharField(max_length=75, unique=True)
    slug = models.SlugField()
    user = models.ForeignKey('User', on_delete=models.CASCADE)