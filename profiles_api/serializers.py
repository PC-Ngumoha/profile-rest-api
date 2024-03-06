from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serializes the API response from the view"""
    name = serializers.CharField(max_length=10)
