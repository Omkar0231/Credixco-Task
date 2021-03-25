from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveAPIView

#models
from users.models import User
from django.contrib.auth.models import Group

#serializer
from users.serializers.user_serializer import ShowUserSerializer

#permissions
from rest_framework.permissions import IsAuthenticated
from users.permissions.is_student import IsStudent


class GetStudentProfileAPIView(RetrieveAPIView):
    '''
    This is the API which is called by the student to know his profile details.
    The permission_classes will check if the user is logged in and is a student.
    '''
    permission_classes = (IsAuthenticated,IsStudent)
    serializer_class = ShowUserSerializer

    def get(self,request,*args,**kwargs):
        serializer = self.serializer_class(request.user)
        return Response({'student-profile':serializer.data},status=status.HTTP_200_OK)