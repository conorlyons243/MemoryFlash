from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Deck(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) # Check this works, docs say only changes on Model.save()

    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Card(models.Model):
    id = models.AutoField(primary_key=True)
    front = models.TextField(max_length=1500)
    back = models.TextField(max_length=1500)

    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    
