from rest_framework import serializers

#models
from users.models import User


class CreateUserSerializer(serializers.ModelSerializer):

    def save(self, validated_data):
        user = User.objects.create_user(validated_data['email'],
             validated_data['password'],name=validated_data['name'],
             father_name=validated_data['father_name'],date_of_birth=validated_data['date_of_birth'],
             gender=validated_data['gender'])
        return user

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'name'          : {'required' : True},
            'father_name'   : {'required' : True},
            'date_of_birth' : {'required' : True},
            'gender'        : {'required' : True},
        }


class ShowUserSerializer(serializers.ModelSerializer):
    groups = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ('id','email','name','father_name','date_of_birth','gender','groups')

    def get_groups(self,obj):
        list_ = []
        for g in obj.groups.all():
            list_.append(g.name)
        return list_


