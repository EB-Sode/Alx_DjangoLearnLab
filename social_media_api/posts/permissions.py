from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    '''Only allow user of the post/comments to delete it'''

    def has_object_permission(self, request, view, obj):
        #safe methods = GET, OPTIONS, HEAD
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.author == request.user