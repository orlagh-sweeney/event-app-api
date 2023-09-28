from django.db import IntegrityError
from rest_framework import serializers
from .models import Attendee


class AttendeeSerializer(serializers.ModelSerializer):
    """
    Serializer for the Attendee model
    The create method handles the unique constraint on 'owner' and 'event'
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Attendee
        fields = [
            'id', 'owner', 'event', 'created_at',
        ]

    # handle duplicates
    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
