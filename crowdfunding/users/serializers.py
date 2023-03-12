from rest_framework.validators import UniqueValidator
from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.password_validation import validate_password
class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=200)
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())]
        )
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'password', 'email')
    def create(self, validated_data):
        user = CustomUser.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class ChangePasswordSerializer(serializers.Serializer):
    model = CustomUser

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

class CustomUserSerializerUpdate(CustomUserSerializer):
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username',instance.username)
        instance.email = validated_data.get('email', instance.email)
        if password := validated_data.get('password'):
            instance.set_password(password)
        instance.save()
        return instance

##### DRAFT 1 ####
# class CustomUserSerializer(serializers.Serializer):
#     id = serializers.ReadOnlyField()
#     username = serializers.CharField(max_length=150)
#     email = serializers.EmailField()

#     def create(self, validated_data):
#         return CustomUser.objects.create(**validated_data)

# class CustomUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ['id', 'first_name', 'last_name', 'username', 'email', 'password']
#         read_only_fields = ['id']
#         extra_kwargs = {"password":{"write_only":True}}

#     def create(self, validated_data):
#         user = CustomUser.objects.create(
#             first_name = validated_data['first_name'],
#             last_name = validated_data['last_name'],
#             username = validated_data['username'],
#             email = validated_data['email']
#         )
#         user.set_password(validated_data['password'])
#         user.save()
#         return user
