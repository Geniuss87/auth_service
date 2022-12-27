from rest_framework import serializers
from django.contrib.auth import get_user_model

from accounts.send_mail import send_message_to_mail

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(min_length=5, write_only=True)
    password2 = serializers.CharField(min_length=5, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

    def validate_email(self, data):
        user = User.objects.filter(email=data).exists
        if not user:
            raise serializers.ValidationError(f'this {data} already exist')
        return data

    def validate(self, attrs):
        password1 = attrs.get('password1')
        password2 = attrs.pop('password2')
        if password1 != password2:
            raise serializers.ValidationError(f'passwords missmatch')
        return attrs

    def create(self, validated_data):
        password = validated_data.pop('password1')
        user = User.objects.create_user(**validated_data, password=password)
        send_message_to_mail(validated_data.get('email'))
        return user