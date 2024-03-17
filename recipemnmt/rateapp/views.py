from django.shortcuts import render
# from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated

from recipeapp.models import Recipe
from rest_framework import mixins,generics,viewsets #import mixins
from rateapp.models import Review
from rateapp.serializers import ReviewSerializer
from rest_framework.views import  APIView
from rest_framework.response import  Response
from django.http import Http404
from rest_framework import status
from rest_framework import status

# Create your views here.

# class ReviewCreate(generics.CreateAPIView):
#     permission_classes = [AllowAny,]
#
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

# class ReviewCreate(APIView):
#     permission_classes = [IsAuthenticated,]
#     def post(self,request,pk):
#         r=Recipe.objects.get(pk=pk)
#         u=self.request.user
#         review=Review.objects.get(user=u,Recipe=r)
#         return Response(status=status.HTTP_200_OK)

class ReviewListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated,]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated,]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

# class ReviewList(generics.ListAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

class ReviewOne(APIView):
    def get_object(self,request,pk):
        try:
            return Recipe.objects.get(pk=pk)
        except:
            raise Http404

    def get(self,request,pk):
        c=self.get_object(request,pk)
        p=Review.objects.filter(recipe=c)
        prod=ReviewSerializer(p,many=True)
        return Response(prod.data)