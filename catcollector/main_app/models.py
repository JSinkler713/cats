from django.db import models

# Anytime we add a new model or modify a model's properties/columns/fields, we need to generate a migrations file
# Once a new migration file is created, we need to run it

# This tuple of tuples will be used to fill in values to a <select> input
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

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