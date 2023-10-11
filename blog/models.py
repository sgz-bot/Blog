from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    nom = models.CharField(max_length=100)
    prenoms = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.nom


class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    createdDate = models.DateField(auto_now=True)
    updateDate = models.DateField()
    tag = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images", default="An image")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default="The autor")

    def __str__(self):
        return self.title


class Categorie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()