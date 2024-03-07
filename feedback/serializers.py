from django.db import IntegrityError
from rest_framework import serializers
from .models import Feedback

class FeedbackSerializer(serializers.ModelSerializer):
    """
    Serializer for the Feedback model
    The create method handles the unique constraint on 'owner' and 'beat'
    """

    class Meta:
        model = Feedback
        fields = '__all__'

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'Feedback already exists for this owner and beat.'
            })
