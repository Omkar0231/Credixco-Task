from rest_framework.permissions import BasePermission
from django.contrib.auth.models import Group

class IsTeacher(BasePermission):
    '''
    This class returns True if the user is belong to the Teachers Group.
    '''
    def has_permission(self, request, view):
        #Checking if the user is a Teacher
        try:
            return Group.objects.get(name='Teachers').user_set.filter(id=request.user.id).exists()
        except Group.DoesNotExist:
            return None
