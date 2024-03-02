from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import CarsSerializer
from .models import Cars
from rest_framework.response import Response
from rest_framework import status
from .permission import IsAuthenticatedOrReadOnly

# Create your views here.
class FetchCarView(APIView):
    permission_classes =[IsAuthenticatedOrReadOnly]
    def get(self, req, id=None):
        print("called")
        if id:
            car = Cars.objects.filter(id=id).first()
            if not car:
                return Response({"success": False, "message": "Car Doesn't Exists...!"}, status=status.HTTP_400_BAD_REQUEST)
            serializer = CarsSerializer(car)
            return Response({"success": True, "message": "Car Fetched Successfully...!", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"success": False, "message": "Id Is Required...!"}, status=status.HTTP_400_BAD_REQUEST)



class FetchCarsView(APIView):
    permission_classes =[IsAuthenticatedOrReadOnly]

    def get(self, req):
        cars = Cars.objects.all()
        serializer = CarsSerializer(cars, many=True)
        return Response({"success": True, "message": "Cars Fetched Successfully...!", "data": serializer.data}, status=status.HTTP_200_OK)

class CreateCarView(APIView):
    permission_classes =[IsAuthenticatedOrReadOnly]

    def post(self, req):
        serializer = CarsSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"success": True, "message": "Car Created Successfully...!", "data": serializer.data}, status=status.HTTP_201_CREATED)

class UpdateCarView(APIView):
    permission_classes =[IsAuthenticatedOrReadOnly]

    def patch(self, req, id=None):
        car = Cars.objects.filter(id=id).first()
        if not car:
                return Response({"success": False, "message": "Car Doesn't Exists...!"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = CarsSerializer(item, data=req.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"success": True, "message": "Car Updated Successfully...!", "data": serializer.data}, status=status.HTTP_201_CREATED)


class DeleteCarView(APIView):
    permission_classes =[IsAuthenticatedOrReadOnly]
    def delete(self, req, id=None):
        car = Cars.objects.filter(id=id).first()
        if not car:
            return Response({"success": False, "message": "Car Doesn't Exists...!"}, status=status.HTTP_400_BAD_REQUEST)
        car.delete()
        return Response({"success": True, "message": "Car Deleted Successfully"}, status=status.HTTP_200_OK)
