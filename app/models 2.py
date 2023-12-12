from django.db import models

# Create your models here.


class Task(models.Model):
    subject = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

# Es para convertir un objeto en cadena de texto
    def __str__(self):
        return self.subject
