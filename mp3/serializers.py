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
        mp3_file = validated_data.get('mp3')  # Get the actual file object

        cloudinary_public_id = f'mp3_file_{validated_data["title"]}_{mp3_file.name}' if mp3_file else None
        print(f"Constructed public_id: {cloudinary_public_id}")

        cloudinary_options = {
            'resource_type': 'auto',
            'public_id': cloudinary_public_id,

         }

        try:
            if mp3_file:
                result = upload(mp3_file, **cloudinary_options)
                print(f"Secure URL before modification: {result.get('secure_url')}")

                validated_data['mp3'] = result.get('secure_url')  # Use 'secure_url' from the Cloudinary result
                print(f"Secure URL after modification: {validated_data['mp3']}")
                
        except Exception as e:
            # Handle the exception (e.g., raise a serializers.ValidationError)
            print(f"Secure URL: {validated_data['mp3']}")
            raise serializers.ValidationError(f"Error uploading mp3 file: {e}")
            
        # Continue with the standard create logic
        return super().create(validated_data)




    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(owner=user, mp3=obj).first()
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
