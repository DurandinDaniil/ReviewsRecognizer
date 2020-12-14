from django.db import models

class Review(models.Model):
    text = models.TextField()
    score = models.IntegerField(null = True)
    mark = models.IntegerField(null = True)

