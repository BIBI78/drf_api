from rest_framework import serializers
from cloudinary.uploader import upload
from mp3.models import Mp3
from likes.models import Like

class Mp3Serializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()

    def create(self, validated_data):
        mp3 = validated_data.get('mp3')  
        # Cloudinary integration code
        cloudinary_options = {
            'resource_type': 'auto',
            'public_id': 'unique_id_for_file',
        }

        try:
            result = upload(mp3, **cloudinary_options)
            validated_data['mp3'] = result['secure_url']
        except Exception as e:
            # Handle the exception (e.g., raise a serializers.ValidationError)
            raise serializers.ValidationError(f"Error uploading mp3 file: {e}")

        # Continue with the standard create logic
        return super().create(validated_data)

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            print('LIKES: ', Like.objects.all())
            like = Like.objects.filter(
                owner=user, mp3=obj
            ).first()
            return like.id if like else None
        return None        

    class Meta:
        model = Mp3
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'title', 'content', 'mp3',
            'like_id', 'likes_count', 'comments_count',
        ]
