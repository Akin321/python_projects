from django.db import models

# Create your models here.
class Food(models.Model):
    name=models.CharField(max_length=150)
    desc=models.TextField()
    price=models.IntegerField()
    img=models.ImageField(upload_to='gallery')

    def __str__(self):
        return self.name