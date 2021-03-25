from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveAPIView

#models
from users.models import User
from django.contrib.auth.models import Group

#serializer
from users.serializers.user_serializer import CreateUserSerializer,ShowUserSerializer
from users.serializers.login_serializer import UserLoginSerializer

#permissions
from rest_framework.permissions import IsAuthenticated
from users.permissions.is_student import IsStudent
from users.permissions.is_superAdmin import IsSuperAdmin
from users.permissions.is_teacher import IsTeacher



class AddUsersAPIView(CreateAPIView):
    '''
    This is the API which is only accessible by the Super Admin where he can 
    create any type of user in the database.
    '''
    permission_classes = (IsAuthenticated,IsSuperAdmin)
    serializer_class = CreateUserSerializer

    def post(self,request,*args,**kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            role = request.data.get('role')
            roles_list = ['TEACHER','STUDENT','SUPER_ADMIN']
            if role in roles_list:
                user = serializer.save(validated_data=request.data)
                #Create a group if doesn't exist or else get the group
                if role=='TEACHER':
                    group, created = Group.objects.get_or_create(name='Teachers')
                elif role=='STUDENT':
                    group, created = Group.objects.get_or_create(name='Students')
                elif role=='SUPER_ADMIN':
                    group, created = Group.objects.get_or_create(name='Super_Admin')
                
                group.user_set.add(user)
                user_serializer = ShowUserSerializer(user)
                return Response({'created_user' : user_serializer.data},status=status.HTTP_201_CREATED)
            
            else:
                return Response({'field_required':'Value of role should be TEACHER or STUDENT or SUPER_ADMIN'},status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response({'error' : serializer.errors},status=status.HTTP_400_BAD_REQUEST)
    


class GetUsersAPIView(RetrieveAPIView):
    '''
    This is the API which gets all the users of the database with a filtering
    that which which user belongs to which group.
    '''
    permission_classes = (IsAuthenticated,IsSuperAdmin)
    serializer_class = ShowUserSerializer

    def get(self,request,*args,**kwargs):
        group_by_value = {}
        qs = User.objects.filter(groups__name='Students')
        group_by_value['Students'] = self.serializer_class(qs,many=True).data
        print(group_by_value)
        qs = User.objects.filter(groups__name='Teachers')
        group_by_value['Teachers'] = self.serializer_class(qs,many=True).data
        qs = User.objects.filter(groups__name='Super_Admin')
        group_by_value['Super_Admins'] = self.serializer_class(qs,many=True).data
        return Response(group_by_value,status=status.HTTP_200_OK)