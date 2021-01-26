from django.db import models

class books(models.Model):
    title=models.CharField(max_length=100)
    subtitle=models.CharField(max_length=100)
    description=models.CharField(max_length=200)
    price=models.IntegerField()
    genre=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    year=models.IntegerField()
    date=models.DateTimeField(auto_now_add=True)

