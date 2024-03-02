
from rest_framework.permissions import BasePermission
from utils.error import errorHandler
from  users.models import User
import jwt

class IsAuthenticatedOrReadOnly(BasePermission):
    """
    Custom permission to allow authenticated users to access the view,
    but read-only permissions to unauthenticated users.
    """

    def has_permission(self, request,views):
        user = self.authenticate_user(request)
        return user is not None

    def authenticate_user(self, req):
        user = None
        token = req.COOKIES.get("token")
        print("token : ",token)
        if token is None:
            return None
        try:
            payload = jwt.decode(token, "secret_key", algorithms=["HS256"])
        except:
            return None
        user = User.objects.filter(id=payload["id"]).first()
        print("called",user)
        return user
