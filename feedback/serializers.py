from rest_framework import serializers
from .models import FeedbackFire, FeedbackCold, FeedbackHard, FeedbackTrash, FeedbackLoop

class FeedbackFireSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackFire
        fields = '__all__'

class FeedbackColdSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackCold
        fields = '__all__'

class FeedbackHardSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackHard
        fields = '__all__'

class FeedbackTrashSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackTrash
        fields = '__all__'

class FeedbackLoopSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackLoop
        fields = '__all__'
