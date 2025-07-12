from django.db import models

# Create your models here.
class Administrador(models.Model):
    user = models.CharField(max_length=50, unique=True)
    passwo = models.CharField(max_length=100)

    def __str__(self):
        return self.user