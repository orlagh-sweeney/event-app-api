from django.db import IntegrityError
from rest_framework import serializers
from .models import Interest


class InterestSerializer(serializers.ModelSerializer):
    """
    Serializer for the Interest model
    The create method handles the unique constraint on 'owner' and 'type'
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Interest
        fields = [
            'id', 'owner', 'type', 'created_at',
        ]

    # handle duplicates
    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
