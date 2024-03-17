from django.db import models

# Create your models here.
class Recipe(models.Model):
    recipe_title=models.CharField(max_length=20)
    recipe_desc=models.CharField(max_length=200)
    recipe_ingredients=models.CharField(max_length=200)
    recipe_instructions=models.CharField(max_length=500)
    recipe_date=models.DateTimeField()
    def __str__(self):
        return self.recipe_title

