from rest_framework.permissions import BasePermission
from django.contrib.auth.models import Group

class IsSuperAdmin(BasePermission):
    '''
    This class returns True if the user is belong to the Super_Admin Group.
    '''
    def has_permission(self, request, view):
        #Checking if the user is a SuperAdmin
        try:
            return Group.objects.get(name='Super_Admin').user_set.filter(id=request.user.id).exists()
        except Group.DoesNotExist:
            return None

