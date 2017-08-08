from rest_framework import serializers
from api.models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('first_name', 'last_name')

class MemberSerialzer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Member
        fields = ('user', 'mobile')

class NewsSerializer(serializers.ModelSerializer):
    publishedBy = MemberSerialzer()

    class Meta:
        model = News
        fields = ('__all__')

class SIGSerializer(serializers.ModelSerializer):
    coordinators = MemberSerialzer(many=True)

    class Meta:
        model = SIG
        fields = ('__all__')

class EventSerializer(serializers.ModelSerializer):
    coordinators = MemberSerialzer(many=True)

    class Meta:
        model = Event
        fields = ('__all__')

class CouncilMemberSerializer(serializers.ModelSerializer):
    member = MemberSerialzer()

    class Meta:
        model = CouncilMember
        fields = ('__all__')