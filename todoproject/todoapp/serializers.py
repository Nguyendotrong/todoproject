from rest_framework.serializers import ModelSerializer

from .models import User


class UserCreateSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'phone', 'email', 'password',
                  'gender', ]
        extra_kwargs = {
            'password': {
                'write_only': True,
                # "validators": [PasswordValidator(language="VN"), ],
                'style': {'input_type': 'password'}
            },
        }

    # def create(self, validated_data):
    #     user = User(**validated_data)
    #     user.set_password(validated_data['password'])
    #     user.save()
    #
    #     return user


class UserSerializer(ModelSerializer):
    class Meta:
        model = User

        exclude = ['password']
        read_only_fields = ["date_joined", 'id', 'username', 'groups']
