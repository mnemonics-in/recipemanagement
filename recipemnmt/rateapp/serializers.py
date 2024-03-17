from rest_framework import serializers
from rateapp.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields=['recipe','user','rating','comment']
