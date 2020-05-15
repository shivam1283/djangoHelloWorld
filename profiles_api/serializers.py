from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
	"""Serializes a name field for esting out APIView"""
	name=serializers.CharField(max_length=10)
