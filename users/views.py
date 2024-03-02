from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializer import UserSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from utils.jwt import sendToken




class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=["POST"])
    def create_user(self, req):
        email = req.data.get("email")
        if not email:
            return Response({
                "success": False,
                "message": "Email Is Required...!"
            }, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.filter(email=email)
        if user :
            return Response({
                "success": False,
                "message": "User Is Already Exists...!"
            }, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.serializer_class(data=req.data or None)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()
        return Response({
                "success": True,
                "message": "User Is Craeted...!",
                "data" : serializer.data
            }, status=status.HTTP_201_CREATED)


    @action(detail=False, methods=["POST"])
    def login_user(self, req): 
        email = req.data.get("email")
        password = req.data.get("password")
        if not email or not password:
            return Response({
                "success": False,
                "message": "All fields are Required...!"
            }, status=status.HTTP_400_BAD_REQUEST)
        
        user = User.objects.filter(email=email).first()
        if not user :
            return Response({
                "success": False,
                "message": "User Doesn't Exists...!"
            }, status=status.HTTP_400_BAD_REQUEST)
        
        return sendToken(user)
