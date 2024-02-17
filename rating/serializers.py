# rating/serializers.py
from rest_framework import serializers
from django.contrib.humanize.templatetags.humanize import naturaltime
from .models import Rating
from django.db import IntegrityError

class RatingSerializer(serializers.ModelSerializer):
    """
    Serializer for the ratings model.
    """
    
    owner = serializers.ReadOnlyField(source='owner.username')
    
    # what shoudl i use for event ?
    class Meta:
        model = Rating
        fields = ['id', 'owner', 'rating', 'beat', 'created_at']
       
        
    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({'detail': 'possible duplicate'})