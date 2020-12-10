from django.db import models
from sweets.models import Pictures

# Create your models here.


class Card(models.Model):
    name = models.CharField(max_length=254)
    content = models.TextField()
    picture = models.OneToOneField(Pictures, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
