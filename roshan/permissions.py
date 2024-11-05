from rest_framework.permissions import BasePermission,IsAuthenticated,IsAdminUser,AllowAny,SAFE_METHODS



class PermCreateApi(BasePermission):
    def has_permission(self, request, view):
        user=request.user
        return bool( user.is_authenticated or  user.is_superuser)

# obj.author==user or 
    
class ReterivePermCreateOrDeleteApi(BasePermission):
    def has_object_permission(self, request, view, obj):
        user=request.user
        if user.is_authenticated or user.is_superuser:
            if obj.author==user:
                return True
            else:
                return False
        else:
            return False
        