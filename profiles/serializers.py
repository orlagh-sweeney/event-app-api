from rest_framework import serializers
from .models import Profile
from interests.models import Interest


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    events_count = serializers.ReadOnlyField()
    attended_count = serializers.ReadOnlyField()
    attending_count = serializers.ReadOnlyField()
    user_interests = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    # get all interests belonging to a profile
    def get_user_interests(self, obj):
        interests = Interest.objects.all()
        user_interests = {}
        for i in interests:
            owner = str(i.owner)
            if owner not in user_interests.keys():
                user_interests[owner] = [i.type]
            else:
                user_interests[owner] = user_interests[owner] + [i.type]
        if str(obj.owner) not in user_interests:
            return None
        else:
            return user_interests[str(obj.owner)]

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'name',
            'content', 'image', 'is_owner', 'events_count', 'attended_count',
            'attending_count', 'user_interests',
        ]
