from rest_framework import serializers

from hello.models import HelloWorld


class HelloWorldSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        return HelloWorld.objects.create(**validated_data)

    hello_world = serializers.CharField()
