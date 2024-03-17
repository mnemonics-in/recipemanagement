from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.models import User
from recipeapp.models import Recipe
from recipeapp.serializers import UserSerializer,RecipeSerializer
from rest_framework import viewsets #import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import  APIView
from rest_framework.response import  Response
from rest_framework import status
from django.http import Http404

# Create your views here.

class CreateUser(viewsets.ModelViewSet):
    queryset =User.objects.all()
    serializer_class = UserSerializer

class AllRecipe(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated,]
    queryset =Recipe.objects.all()
    serializer_class = RecipeSerializer
#
# class Recipeview(APIView):
#     permission_classes = [IsAuthenticated]
#     def get(self,request):
#         u=self.request.user
#         rec=Recipe.objects.filter(user=u)
#         c=RecipeSerializer(rec,many=True)
#         return Response(c.data)
class user_logout(APIView):
    permission_classes =[IsAuthenticated,]
    def get(self,request):
        self.request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


# class RecipeDetails(APIView): #Non primary key
#     # permission_classes = [IsAuthenticated, ]
#     def get(self, request):
#         rec= Recipe.objects.all()
#         r = RecipeSerializer(rec, many=True)
#         return Response(r.data)
    # def post(self, request):
    #     s = RecipeSerializer(data=request.data)
    #     if s.is_valid():
    #         s.save()
    #         return Response(s.data, status=status.HTTP_201_CREATED)
    #     return Response(status=status.HTTP_400_BAD_REQUEST)
