from django.shortcuts import render
from recipeapp.models import Recipe
from django.db.models import Q
from rest_framework.views import  APIView
from recipeapp.serializers import RecipeSerializer
from rest_framework.response import  Response
# Create your views here.
class search(APIView):
    def get(self,request):
        #to get the keyword for search from the request query parameters send from client
        query=self.request.query_params.get('search') #{param:{'search':'carrot'}} # default key search
        if(query):
            recipe=Recipe.objects.filter(Q(recipe_ingredients__icontains=query) | Q(recipe_desc__icontains=query))
            r=RecipeSerializer(recipe,many=True)
            return Response(r.data)