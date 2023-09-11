from rest_framework import serializers
from .models import Event
from attendees.models import Attendee
from datetime import date


class EventSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    attending_id = serializers.SerializerMethodField()
    attending_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()
    is_live = serializers.SerializerMethodField()

    # valiate image sizes
    def validate_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    # check if a user is attending an event
    def get_attending_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            attending = Attendee.objects.filter(
                owner=user, event=obj
            ).first()
            return attending.id if attending else None
        return None

    # check if an event is live
    def get_is_live(self, obj):
        today = date.today()
        return obj.date >= today

    class Meta:
        model = Event
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'title', 'date',
            'time', 'location', 'content', 'image', 'is_owner', 'profile_id',
            'profile_image', 'type', 'attending_id', 'attending_count',
            'comments_count', 'is_live'
        ]
