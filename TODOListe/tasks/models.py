from django.db import models
from django.utils.text import slugify

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username

class Task(models.Model):
    name = models.CharField(max_length=75)
    description = models.TextField()
    categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Categorie(models.Model):
    name = models.CharField(max_length=75)
    slug = models.SlugField()
    user = models.ForeignKey('User', on_delete=models.CASCADE)

    @classmethod
    def get_default_categorie(cls, user):
        collection, _ = cls.objects.get_or_create(name="Defaut", slug="_defaut", user=user)
        return collection

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name