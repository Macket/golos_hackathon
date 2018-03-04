from rest_framework import serializers


class VideoSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)