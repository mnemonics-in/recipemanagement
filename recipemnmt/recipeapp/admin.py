from django.contrib import admin
from recipeapp.models import Recipe
from rateapp.models import Review
# Register your models here.
admin.site.register(Recipe)
admin.site.register(Review)
