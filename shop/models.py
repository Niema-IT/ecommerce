from django.db import models
from django.db.models import ForeignKey


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.name        


class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    category = ForeignKey(Category, related_name= 'categorie', on_delete=models.CASCADE)
    image = models.CharField(max_length=5000)
    image_1 = models.CharField(max_length=500)
    image_2 = models.CharField(max_length=500)
    image_3 = models.CharField(max_length=500)
    image_4 = models.CharField(max_length=500)
    image_5 = models.CharField(max_length=500)
    date_added = models.DateTimeField(auto_now=True)
    disponibilite = models.CharField(max_length=100, default="DISPONIBLE")
    class Meta:
        ordering = ['-date_added']
    
    def __str__(self):
        return self.title
    
class Commande(models.Model):
    items = models.CharField(max_length=300)
    total = models.CharField(max_length=200)
    nom = models.CharField(max_length=150)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    ville = models.CharField(max_length=200)
    pays = models.CharField(max_length=300)
    zipcode = models.CharField(max_length=300)
    file = models.ImageField(max_length=150)
    date_commande = models.DateTimeField(auto_now=True)

    class Meta:
         ordering = ['-date_commande']

    def __str__(self):
        return self.nom

