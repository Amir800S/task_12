from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    pseudonym = models.CharField(max_length=150)
    birthday = models.DateField()

