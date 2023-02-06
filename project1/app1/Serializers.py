from rest_framework import serializers
from .models import Mobile


class MobileSerializers(serializers.ModelSerializer):
    owner = serializers.CharField(read_only=True) 
    class Meta:
        model = Mobile
        fields = '__all__'

    def create(self, validated_data):
        User = self.context.get('request').user
        validated_data.update({'owner':str(User)})
        return Mobile.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.owner = validated_data.get('owner', instance.owner)
        return instance