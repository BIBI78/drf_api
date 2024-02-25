from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Form

class FormSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context.get('request')
        return request.user == obj.owner

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)
    
    def get_updated_at(self, obj):
        return None  # Since 'updated_at' doesn't exist in the Form model, return None

    class Meta:
        model = Form
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image',
             'beat', 'created_at', 'content', 'updated_at'
        ]

class FormDetailSerializer(FormSerializer):
    beat = serializers.ReadOnlyField(source='beat.id')
