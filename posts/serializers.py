from rest_framework import serializers
from posts.models import Post
from likes.models import Like
from django.conf import settings
from cloudinary.uploader import upload

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    # comments_count = serializers.ReadOnlyField()

    mp3_url = serializers.SerializerMethodField()

    def get_mp3_url(self, obj):
        print(obj.mp3)
        return str(obj.mp3)

    def create(self, validated_data):
        mp3_file = validated_data.pop('mp3', None)  # Pop mp3 file from validated_data
        instance = super().create(validated_data)  # Create the instance without mp3

        if mp3_file:
            # Upload mp3 file to Cloudinary
            cloudinary_options = {
                'resource_type': 'auto',
                'public_id': f'mp3_file_{instance.title}_{mp3_file.name}'
            }
            try:
                result = upload(mp3_file, **cloudinary_options)
                instance.mp3 = result.get('secure_url')  # Use 'secure_url' from the Cloudinary result
            except Exception as e:
                raise serializers.ValidationError(f"Error uploading mp3 file: {e}")

        instance.save()  # Save the instance with mp3 file

        return instance

    def validate_image(self, value):
        # Your image validation logic here
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(owner=user, post=obj).first()
            return like.id if like else None
        return None

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'title', 'content', 'mp3', 'image',
            'like_id', 'likes_count', 'mp3_url'
        ]
