from rest_framework import serializers
from recipeapp.models import Recipe
from django.contrib.auth.models import User

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Recipe
        fields=['id','recipe_title','recipe_desc','recipe_ingredients','recipe_instructions','recipe_date']

class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=['id','username','password']
    def create(self, validated_data):  # after validation
        u = User.objects.create_user(username=validated_data['username'], password=validated_data['password'])
        u.save()
        return u