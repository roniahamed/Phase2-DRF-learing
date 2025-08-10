from rest_framework import serializers
from .models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}, write_only = True)

    class Meta:
        Model = User 
        fields = ['email', 'first_name', 'last_name', 'password', 'password2']
        extra_keyword = {
            'password':{'write_only':True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password':"Password didn't match"})
        return attrs
    
    def save(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        return user
