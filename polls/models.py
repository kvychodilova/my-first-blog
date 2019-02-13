from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=128, default="")
    category = models.ForeignKey('Category',on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title
        return self.name
        #vypíše přímo název



class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name