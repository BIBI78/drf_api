from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers

class CurrentUserSerializer(UserDetailsSerializer):
    """
    Serializer for the current user, extending UserDetailsSerializer from dj_rest_auth.
    """
    # Additional fields to include in the serializer
    profile_id = serializers.ReadOnlyField(source='profile.id')  # Read-only field for the profile ID
    profile_image = serializers.ReadOnlyField(source='profile.image.url')  # Read-only field for the profile image URL

    class Meta(UserDetailsSerializer.Meta):
        """
        Meta class defining metadata for the serializer.
        """
        # Include all fields from UserDetailsSerializer and add the additional fields
        fields = UserDetailsSerializer.Meta.fields + (
            'profile_id', 'profile_image'
        )
