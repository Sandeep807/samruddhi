from django.shortcuts import render
from .serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import status

class CustomerView(APIView):
    def post(self,request):
        try:
            serializer=CustomerSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status':'Success',
                    "message":"Data has been saved",
                    "data":serializer.data
                })
            else:
                return Response({
                    'message':serializer.errors
                },status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response({
                'message':'Something went wrong'
            },status=status.HTTP_204_NO_CONTENT)
        
    def get(self,request):
        try:
            mobile_number=request.GET.get('mobile_number')
            cus=Customer.objects.filter(mobile_number=mobile_number).first()
            if cus is not None:
                serialiser=CustomerSerializer(cus)
                return Response({
                    'status':'Success',
                    'data':serialiser.data
                })
            else:
                return Response({
                    'message':'Mobile number not found'
                },status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(e)
            return Response({
                'message':'Something went wrong'
            },status=status.HTTP_204_NO_CONTENT)

class LoginView(APIView):
    def post(self,request):
        try:
            data=request.data
            serializer=LoginSerialiser(data=data)
            if serializer.is_valid():
                username=serializer.data['username']
                password=serializer.data['password']
                obj=authenticate(username=username,password=password)
                if obj is not None:
                    return Response({
                        'status':'Success',
                        'Message':'Login successful'
                    })
                else:
                    return Response({
                        'Message':'Invalid username and password'
                    },status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(e)
            return Response({
                'Message':'Something went wrong'
            },status=status.HTTP_204_NO_CONTENT)
    
