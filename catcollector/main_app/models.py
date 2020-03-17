from django.db import models

# Anytime we add a new model or modify a model's properties/columns/fields, we need to generate a migrations file
# Once a new migration file is created, we need to run it

# Create your models here.
# Inherit functionality from Django's models
class Cat(models.Model):
    # defines columns for our Cat table and gives them datatypes and max_lengths
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    # Makes sure we print the cats name and not a confusing model object
    def __str__(self):
        return self.name