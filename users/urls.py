
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

route = DefaultRouter()

route.register(r'user',UserViewSet,basename="user")

urlpatterns = route.urls