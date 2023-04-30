from django.db import models

# Create your models here

class PortfolioDoc(models.Model):
    title = models.TextField()
    document = models.FileField()

