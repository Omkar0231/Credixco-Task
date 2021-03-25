from rest_framework.views import APIView
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



class AddStudentsAPIView(CreateAPIView):
    '''
    This is the api which is accessible only by teachers to create 
    the students. In the questions it is give that, Teacher can add or list
    the students. So, here i am assuming that Teacher should create the
    students and get the students.
    '''
    permission_classes = (IsAuthenticated,IsTeacher)
    serializer_class = CreateUserSerializer

    def post(self,request,*args,**kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save(validated_data=request.data)
            group, created = Group.objects.get_or_create(name='Students')
            group.user_set.add(user)
            user_serializer = ShowUserSerializer(user)
            return Response({'message': 'Student is created successfully.','student_details': user_serializer.data},status=status.HTTP_201_CREATED)
        else:
            return Response({'error':serializer.errors},status=status.HTTP_400_BAD_REQUEST)


class GetStudentsAPIView(RetrieveAPIView):
    '''
    This is the api which is accessible only by the teacher which lets the 
    teacher to see all the student available.
    '''
    permission_classes = (IsAuthenticated,IsTeacher)
    serializer_class = ShowUserSerializer

    def get(self,request,*args,**kwargs):
        qs = User.objects.filter(groups__name='Students')
        serializer = self.serializer_class(qs,many=True)
        return Response({'students':serializer.data},status=status.HTTP_200_OK)