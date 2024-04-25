from rest_framework import serializers
from beats.models import Beat
from likes.models import Like
from feedback.models import (
    FeedbackFire,
    FeedbackCold,
    FeedbackHard,
    FeedbackTrash,
    FeedbackLoop,
)
from django.conf import settings
from cloudinary.uploader import upload


class BeatSerializer(serializers.ModelSerializer):
    """
    Serializer for the Beat model.
    """

    # Read-only fields
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()
    mp3_url = serializers.SerializerMethodField()

    # Feedback fields
    fire_id = serializers.SerializerMethodField()
    cold_id = serializers.SerializerMethodField()
    hard_id = serializers.SerializerMethodField()
    trash_id = serializers.SerializerMethodField()
    loop_id = serializers.SerializerMethodField()
    fire_count = serializers.ReadOnlyField()
    cold_count = serializers.ReadOnlyField()
    hard_count = serializers.ReadOnlyField()
    trash_count = serializers.ReadOnlyField()
    loop_count = serializers.ReadOnlyField()

    def get_mp3_url(self, obj):
        """
        Get the URL for the MP3 file.
        """
        print(obj.mp3)
        return str(obj.mp3)

    def create(self, validated_data):
        """
        Create a new Beat instance.
        """
        mp3_file = validated_data.pop('mp3', None)
        # Pop mp3 file from validated_data
        instance = super().create(validated_data)
        # Create the instance without mp3

        if mp3_file:
            # Upload mp3 file to Cloudinary
            cloudinary_options = {
                'resource_type': 'video',
                'public_id': f'mp3_file_{instance.title}_{mp3_file.name}'
            }
            try:
                result = upload(mp3_file, **cloudinary_options)
                instance.mp3 = result.get('secure_url')
                # Use 'secure_url' from the Cloudinary result
            except Exception as e:
                raise serializers.ValidationError(
                    f"Error uploading mp3 file: {e}"
                )

            instance.save()  # Save the instance with mp3 file

        return instance

    def update(self, instance, validated_data):
        """
        Update an existing Beat instance.
        """
        mp3_file = validated_data.get('mp3', None)
        # Pop mp3 file from validated_data
        instance.title = validated_data.get('title', None)
        instance.content = validated_data.get('content', None)

        if mp3_file:
            # Upload mp3 file to Cloudinary
            cloudinary_options = {
                'resource_type': 'video',
                'public_id': f'mp3_file_{instance.title[:10]}_{mp3_file.name}'
            }
            try:
                result = upload(mp3_file, **cloudinary_options)
                instance.mp3 = result.get('secure_url')
                # Use 'secure_url' from the Cloudinary result
                print(f'secure_url: {instance.mp3}')
            except Exception as e:
                raise serializers.ValidationError(
                    f"Error uploading mp3 file: {e}"
                )

            instance.save()  # Save the instance with mp3 file
        else:
            instance.save()

        return instance

    def get_is_owner(self, obj):
        """
        Check if the requesting user is the owner of the Beat.
        """
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        """
        Get the ID of the Like associated with the Beat for the requesting user
        """
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(owner=user, beat=obj).first()
            return like.id if like else None
        return None

    # Methods to get the IDs of different types of feedback associated w/ Beat
    # Similar logic to get_like_id

    # Meta class for defining model and fields
    class Meta:
        model = Beat
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'title', 'content', 'mp3', 'like_id', 'likes_count',
            'comments_count', 'mp3_url', 'cold_count',
            'hard_count', 'trash_count', 'loop_count', 'fire_count',
            'fire_id', 'cold_id', 'hard_id', 'trash_id', 'loop_id',
        ]
