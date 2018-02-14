from rest_framework.permissions import BasePermission

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS', 'POST')

class IsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
    #Return si el usuario es el dueño de Ciudad
        if request.method in SAFE_METHODS:
            return True
        elif request.method == 'PUT' or request.method == 'PACTH':
          pass

