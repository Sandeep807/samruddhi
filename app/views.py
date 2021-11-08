from django.shortcuts import render
from .serializer import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication



"""This api is used to insert data into table and get data from table"""

class CustomerView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self,request):
        try:
            username=request.GET.get('username')
            obj=User.objects.filter(username=username).first()
            print(obj)
            wserializer=UserSerailizer(obj)
            wid=wserializer.data['wallets']
            if len(wid)>0:
                id=wid[0]['id']
                amount=float(request.data['amount_paid'])
                obj1=Wallet.objects.filter(id=id).first()
                serializer=CustomerSerializer(data=request.data)
                if serializer.is_valid():
                    if obj1.wallet>=amount:
                            obj1.wallet=obj1.wallet-amount
                            obj1.save()
                            serializer.save()
                            return Response({
                                    'status':'Success',
                                    "Message":"Data has been saved",
                                    "data":serializer.data
                                })
                    else:
                            return Response({
                                    'Message':'Insuficient balance'
                                },status=status.HTTP_406_NOT_ACCEPTABLE)
                else:
                        return Response({
                            'Message':serializer.errors
                            },status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'Message':'Amount not found'},status=status.HTTP_404_NOT_FOUND)    
        except Exception as e:
            print(e)
            return Response({
                'Message':'Something went wrong'
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
                    'Message':'Mobile number not found'
                },status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(e)
            return Response({
                'Message':'Something went wrong'
            },status=status.HTTP_204_NO_CONTENT)

class CustomerRelease(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self,request):
        try:
            username=request.GET.get('username')
            obj=User.objects.filter(username=username).first()
            serializer=ReleaseCustomerSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status':'Success',
                    "Message":"Data has been saved",
                    "data":serializer.data
                })
            else:
                return Response({
                    'Message':serializer.errors
                },status=status.HTTP_400_BAD_REQUEST) 
        except Exception as e:
            print(e)
            return Response({
                'Message':'Something went wrong'
            },status=status.HTTP_204_NO_CONTENT)


"""This api used to login and get token a particuler agent"""
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
    

"""This api is used to get balance a particuler agent remaining balance"""
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

"""This api is used to post into table"""
class StatusAproved(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]
    def get(self,request):
        try:
            #username=request.GET.get('username')
            # stat=request.dat
            # serializer=CustomerSerializer1(data=stat)
            # if serializer.is_valid():
            #     data=serializer.data['status']
            obj=Customer.objects.filter(status='Aproved')
            if obj:
                serializer=CustomerSerializer(obj,many=True)
                return Response(data=serializer.data,status=status.HTTP_200_OK)
            else:
                return Response({
                    'Message':'Not found'
                },status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(e)
            return Response({
                'Message':'Something went wrong'
            },status=status.HTTP_400_BAD_REQUEST)



"""This api is used to post into table"""
class StatusReject(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]
    def get(self,request):
        try:
            #username=request.GET.get('username')
            # stat=request.dat
            # serializer=CustomerSerializer1(data=stat)
            # if serializer.is_valid():
            #     data=serializer.data['status']
            obj=Customer.objects.filter(status='Reject')
            if obj:
                serializer=CustomerSerializer(obj,many=True)
                return Response(data=serializer.data,status=status.HTTP_200_OK)
            else:
                return Response({
                    'Message':'Not found'
                },status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(e)
            return Response({
                'Message':'Something went wrong'
            },status=status.HTTP_400_BAD_REQUEST)


"""This api is used to get data all customer"""
class AllCustomer(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]
    def get(self,request):
        try:
            customer=Customer.objects.all()
            print(customer)
            if customer is not None:
                serializer=CustomerSerializer(customer,many=True)
                return Response(data=serializer.data,status=status.HTTP_200_OK)
            else:
                return Response({'Message':'No data available'},status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            print(e)
            return Response({
                'Error':'Something went wrong'
            },status=status.HTTP_404_NOT_FOUND)

"""This api is used to get all agent from table"""
class AllAgent(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]
    def get(self,request):
        try:
            user=User.objects.all()
            if user is not None:
                serializer=UserSerailizer(user,many=True)
                return Response(data=serializer.data,status=status.HTTP_200_OK)
            else:
                return Response({
                    'Message':'No data available for agent'
                },status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(e)
            return Response({
                'Message':'Something went wrong'
            },status=status.HTTP_400_BAD_REQUEST)

class GetGoldPrice(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        try:
            obj=GoldPrice.objects.all()
            if obj is not None:
                serializer=GoldPriceSerializer(obj,many=True)
                return Response(data=serializer.data,status=status.HTTP_200_OK)
            else:
                return Response({
                    'Message':'Gold price not available'
                },status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(e)
            return Response({
                'Message':'Something went wrong'
                },status=status.HTTP_400_BAD_REQUEST)