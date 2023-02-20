from rest_framework.permissions import BasePermission
from authapi.models import User
from authapi.options import ROLE_PATIENT, ROLE_THERAPIST
'''
Permissions as implemented by the AuthorityMatrix.
'''

class IsPatient(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        return request.user.role in [ROLE_PATIENT]


class IsTherapist(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        return request.user.role in [ROLE_THERAPIST]


class IsUser(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        return request.user.role in [ROLE_PATIENT, ROLE_THERAPIST]


class JournalBelongsToUser(BasePermission):

    def has_object_permission(self, request, view, obj):
        return (request.user == obj.patient.therapist) or \
            (request.user == obj.patient)
        