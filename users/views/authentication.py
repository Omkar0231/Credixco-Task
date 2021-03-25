from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status

#models
from users.models import User
from django.contrib.auth.models import Group

#serializer
from users.serializers.user_serializer import CreateUserSerializer,ShowUserSerializer
from users.serializers.login_serializer import UserLoginSerializer

#permissions
from rest_framework.permissions import AllowAny

#datetime
import datetime

#This is the API for Signup
class SignUpAPIView(CreateAPIView):
    serializer_class = CreateUserSerializer

    def post(self,request,*args,**kwargs):
        ''' 
        This is a post request where details like email, password,
        name, father_name, date_of_birth, gender and role.
        Here role decides in which group the user should go.
        '''
        # Using the serializer for better validation and send json data in response
        # as it is a Rest API
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            role = request.data.get('role')
            roles_list = ['TEACHER','STUDENT','SUPER_ADMIN']
            if role in roles_list:
                # Checking the date of birth is not current or greater 
                # than current date
                data = request.data.copy()
                date_of_birth = data['date_of_birth']
                date_of_birth = datetime.datetime.strptime(date_of_birth, '%d-%m-%Y')
                date_of_birth = date_of_birth.date()
                if date_of_birth >= datetime.date.today(): 
                    return Response({'error':'Please enter a valid Date of Birth'})
                data['date_of_birth'] = f'{date_of_birth.year}-{date_of_birth.month}-{date_of_birth.day}'
                
                #Saving the user object after all validations
                user = serializer.save(validated_data=data)

                #Create a group for the first time or get it if it already created
                if role=='TEACHER':
                    group, created = Group.objects.get_or_create(name='Teachers')
                elif role=='STUDENT':
                    group, created = Group.objects.get_or_create(name='Students')
                elif role=='SUPER_ADMIN':
                    group, created = Group.objects.get_or_create(name='Super_Admin')
                
                #Adding the user to the respective group according to the given role
                group.user_set.add(user)
                user_serializer = ShowUserSerializer(user)
                return Response({'created_user' : user_serializer.data},status=status.HTTP_201_CREATED)
            else:
                return Response({'field_required':'Value of role should be TEACHER or STUDENT or SUPER_ADMIN'},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error' : serializer.errors},status=status.HTTP_400_BAD_REQUEST)
    



#This is the API for the Login
class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer

    def post(self,request,*args,**kwargs):
        #Here I am using the Login Serializer to authenticate the user
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response({
            'message': 'User logged in  successfully',
            'token' : serializer.data['token'],
            }, status=status.HTTP_200_OK)

