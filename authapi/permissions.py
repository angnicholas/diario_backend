from rest_framework.permissions import BasePermission
from authapi.models import User

'''
Permissions as implemented by the AuthorityMatrix.
'''
class IsEndUser(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        return request.user.role in ['EU']


class IsInstitution(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        return request.user.role in ['IN']


class IsInstitutionOrEndUser(BasePermission):
    def has_permission(self, request, view):        
        if request.user.is_anonymous:
            return False
        return request.user.role in ['IN', 'EU']

