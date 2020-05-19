from django.db import models
from datetime import date
# this import is used with CBVs (see Toy:get_absolute_url())
from django.urls import reverse
# Import the User model provided by Django
from django.contrib.auth.models import User

# Anytime we add a new model or modify a model's properties/columns/fields, we need to generate a migrations file
# Once a new migration file is created, we need to run it

# This tuple of tuples will be used to fill in values to a <select> input
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

# Create your models here.
class Toy(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  # This method is required for CBV usage
  def get_absolute_url(self):
    return reverse('toys_detail', kwargs={'pk': self.id})


# Inherit functionality from Django's models
class Cat(models.Model):
    # defines columns for our Cat table and gives them datatypes and max_lengths
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    # Adds a M:M relationship between Cats and Toys
    toys = models.ManyToManyField(Toy)
    # Adds a 1:M relationship between a User and their Cats
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Makes sure we print the cats name and not a confusing model object
    def __str__(self):
        return self.name

    # add this new method
    def fed_for_today(self):
        return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)

class Photo(models.Model):
    url = models.CharField(max_length=200)
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for cat_id: {self.cat_id} @{self.url}"

# Adds a new model to our DB
class Feeding(models.Model):
    # fields include a Date type column 
    # and a Character (string) type column
    date = models.DateField('feeding date')
    meal = models.CharField(
        max_length=1,
        # add the 'choices' field option (built into Django)
        choices=MEALS,
        # set default meal to Breakfast
        default=MEALS[0][0]
    )
    # this creates the relationship between cats and feedings
    # if the associated cat is removed from the DB, we will remove
    # that cat's feedings
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)

    def __str__(self):
        # show a user-friendly output for the value of Field.choice
        return f'{self.get_meal_display()} on {self.date}'
    
    # use the meta class to change the sorting order
    class Meta:
        ordering = ['-date']
