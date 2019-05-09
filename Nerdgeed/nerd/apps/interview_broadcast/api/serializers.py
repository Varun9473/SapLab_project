from rest_framework import serializers
# from rest_framework.fields import ListField
from apps.interview_broadcast.models import Dashbooard , popupuser


class dashSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dashbooard
        fields = '__all__'


class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = popupuser
        fields = '__all__'
