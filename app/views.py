from django.shortcuts import render
from .serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication

class CustomerView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request):
        try:
            id=request.GET.get('username')
            obj=User.objects.filter(username=id).first()
            wserializer=UserSerailizer(obj)
            wid=wserializer.data['wallets']
            id=wid[0]['id']
            amount=float(request.data['amount_paid'])
            obj1=Wallet.objects.filter(id=id).first()
            print(obj1)
            serializer=CustomerSerializer(data=request.data)
            if serializer.is_valid():
                    if obj1.wallet>=amount:
                        obj1.wallet=obj1.wallet-amount
                        obj1.save()
                        serializer.save()
                        return Response({
                            'status':'Success',
                            "message":"Data has been saved",
                            "data":serializer.data
                        })
                    else:
                        return Response({
                            'message':'Insuficient balance'
                        },status=status.HTTP_406_NOT_ACCEPTABLE)
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
                    token,_ = Token.objects.get_or_create(user=obj)
                    return Response({
                        'status':'Success',
                        'Message':'Login successful',
                        'token':str(token)
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
    

class Balance(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        try:
            user=request.GET.get('username')
            obj=User.objects.filter(username=user).first()
            if obj is not None:
                serializer=UserSerailizer(obj)
                return Response(status=status.HTTP_200_OK,data=serializer.data)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)
