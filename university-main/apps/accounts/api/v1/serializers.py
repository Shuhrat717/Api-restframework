from django.contrib.auth.tokens import PasswordResetTokenGenerator
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from ...models import Account


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, max_length=68, write_only=True)
    password2 = serializers.CharField(min_length=6, max_length=68, write_only=True)

    class Meta:
        model = Account
        fields = ('username', 'password', 'password2')

    def validate(self, attrs):
        password1 = attrs.get('password')
        password2 = attrs.get('password2')
        if password1 != password2:
            raise serializers.ValidationError({'success': False, 'massage': 'Password did not match, please try again'})
        return attrs

    def create(self, validated_data):
        del validated_data['password2']
        return Account.objects.create_user(**validated_data)
