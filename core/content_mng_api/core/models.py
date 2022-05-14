from django.db import models
from django.db.models import Model

class Category(Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    def __str__(self) -> str:
        return f'{self.name},{self.description}'

class Tag(Model):
    title = models.CharField(max_length=100)

class Content(Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    image = models.URLField()
    dealine = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
