from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import SchoolSerializer,StudentSerializer
from rest_framework import viewsets
from rest_framework import status
from rest_framework.authtoken.models import Token

# Create your views here.


# class SchoolViewSet(viewsets.ViewSet):
#     # permission_classes = [IsAuthenticated]
    
#     def list(self, request):
#         stu = SchoolModel.objects.all()
#         serializer = SchoolSerializer(stu, many=True)
#         return Response(serializer.data,safe=False)

#     def retrieve(self, request, pk=None):
#         id = pk
#         if id is not None:
#             stu = SchoolModel.objects.get(id=id)
#             serializer = SchoolSerializer(stu)
#             return Response(serializer.data)

#     def create(self, request):
#         serializer = SchoolSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def update(self,request, pk):
#         id = pk
#         stu = SchoolModel.objects.get(pk=id)
#         serializer = SchoolSerializer(stu, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Complete Data Updated'})
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def partial_update(self,request, pk):
#         id = pk
#         stu = SchoolModel.objects.get(pk=id)
#         serializer = SchoolSerializer(stu, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Partial Data Updated'})
#         return Response(serializer.errors)

#     def destroy(self,request, pk):
#         id = pk
#         stu = SchoolModel.objects.get(pk=id)
#         stu.delete()
#         return Response({'msg':'Data Deleted'})


# class SchoolViewSet(viewsets.ModelViewSet):
#     authentication_classes = [SessionAuthentication, BasicAuthentication]
#     permission_classes = [IsAuthenticated]
#     queryset = School.objects.all()
#     serializer_class = SchoolSerializer



# class SchoolViewSet(viewsets.ModelViewSet):
#     authentication_classes=[SessionAuthentication,BasicAuthentication]# Session funcnalty provid krata hai and basic narmal
#     permission_classes = [IsAuthenticated]
#     queryset = SchoolModel.objects.all()
#     serializer_class = SchoolSerializer




# ===================token=============

class SchoolViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = SchoolModel.objects.all()
    serializer_class = SchoolSerializer


class StudentViewSet(viewsets.ModelViewSet):
    authentication_classes=[IsAuthenticated]
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer
    