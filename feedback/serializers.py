from rest_framework import serializers
from django.db import IntegrityError
from .models import (
    FeedbackFire,
    FeedbackCold,
    FeedbackHard,
    FeedbackTrash,
    FeedbackLoop,
)


class FeedbackFireSerializer(serializers.ModelSerializer):
    """
    Serializer for FeedbackFire model.
    """
    owner = serializers.ReadOnlyField(source='owner.username')  # Read-only

    class Meta:
        model = FeedbackFire
        fields = '__all__'  # Include all fields

    def create(self, validated_data):
        """
        Custom create method to handle possible IntegrityError
        (possible duplicate).
        """
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })


# Repeat for other serializers with similar comments...


class FeedbackColdSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = FeedbackCold
        fields = '__all__'

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })


class FeedbackHardSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = FeedbackHard
        fields = '__all__'

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })


class FeedbackTrashSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = FeedbackTrash
        fields = '__all__'

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })


class FeedbackLoopSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = FeedbackLoop
        fields = '__all__'

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
