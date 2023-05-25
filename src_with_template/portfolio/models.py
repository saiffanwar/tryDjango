from django.db import models

# Create your models here.


class PortfolioDoc(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    document = models.FileField(upload_to='documents/')
