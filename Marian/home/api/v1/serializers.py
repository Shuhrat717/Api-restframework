from rest_framework import serializers
from ...models import Service, About


class MarianSerializer(serializers.ModelSerializer):
    class Meta:
        model = None
        fields = '__all__'

    def set_model(self, model):
        self.Meta.model = model


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('id', 'title')


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ('id', 'title')
