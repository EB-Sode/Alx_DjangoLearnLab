from rest_framework.permissions import BasePermission

class IsAuthenticated(BasePermission):
    
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
    

class IsAdminUser(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        return request.user.is_staff
    
    def has_permission(self, request, view):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
