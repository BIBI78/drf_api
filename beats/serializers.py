from rest_framework import serializers
from beats.models import Beat
from likes.models import Like
from feedback.models import Feedback  # Import the Feedback model
from django.db.models import Count, Case, When, BooleanField

class BeatSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()
    
    # Add SerializerMethodField for each type of feedback
    fire_count = serializers.SerializerMethodField()
    cold_count = serializers.SerializerMethodField()
    hard_count = serializers.SerializerMethodField()
    trash_count = serializers.SerializerMethodField()
    loop_count = serializers.SerializerMethodField()

    mp3_url = serializers.SerializerMethodField()

    # Existing methods remain unchanged

    def get_fire_count(self, obj):
        return obj.feedback_set.filter(fire=True).count()

    def get_cold_count(self, obj):
        return obj.feedback_set.filter(cold=True).count()

    def get_hard_count(self, obj):
        return obj.feedback_set.filter(hard=True).count()

    def get_trash_count(self, obj):
        return obj.feedback_set.filter(trash=True).count()

    def get_loop_count(self, obj):
        return obj.feedback_set.filter(loop=True).count()

    class Meta:
        model = Beat
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'title', 'content', 'mp3', 'image',
            'like_id', 'likes_count', 'comments_count',
            'fire_count', 'cold_count', 'hard_count',
            'trash_count', 'loop_count', 'mp3_url'
        ]
