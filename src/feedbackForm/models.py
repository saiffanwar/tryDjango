from django.db import models

class FeedbackModel(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    message = models.CharField(max_length=200)
