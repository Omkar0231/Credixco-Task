from rest_framework.permissions import BasePermission
from django.contrib.auth.models import Group


class IsStudent(BasePermission):
    '''
    This class returns True if the user is belong to the Students Group.
    '''
    def has_permission(self, request, view):
        #Checking if the user is a Student
        try:
            return Group.objects.get(name='Students').user_set.filter(id=request.user.id).exists()
        except Group.DoesNotExist:
            return None
