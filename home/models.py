from django.db import models

# Create your models here.


class Card(models.Model):
    name = models.CharField(max_length=254)
    content = models.TextField()

    def __str__(self):
        return self.name
