from django.db import models
from django.contrib.auth.models import User
from recipeapp.models import Recipe


# Create your models here.
class Review(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField()

    def __str__(self):
        return f"Review for {self.recipe.recipe_title} by {self.user.username}"