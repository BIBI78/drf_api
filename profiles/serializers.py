from rest_framework import serializers
from .models import Profile
from followers.models import Follower
from beats.models import Beat  # Import the Beat model


class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the Profile model.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()
    beats_count = serializers.SerializerMethodField()  # Change to SerializerMethodField
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        """
        Method to determine if the current user is 
        the owner of the profile.
        """
        request = self.context['request']
        return request.user == obj.owner

    def get_following_id(self, obj):
        """
        Method to get the ID of the following relationship between 
        the current user and the profile owner.
        """
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follower.objects.filter(
                owner=user, followed=obj.owner
            ).first()
            return following.id if following else None
        return None

    def get_beats_count(self, obj):
        """
        Method to get the count of beats owned by the user.
        """
        return Beat.objects.filter(owner=obj.owner).count()

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'name',
            'content', 'image', 'is_owner', 'following_id',
            'beats_count', 'followers_count', 'following_count',
        ]
