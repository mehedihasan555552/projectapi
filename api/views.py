from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import authentication_classes,permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer,JobSerializer,UserSerializer,OrderSerializer
from .models import *
from django.contrib.auth.models import User
import six
import sys
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from rest_framework.utils import json
from rest_framework.response import Response
import requests
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.


from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from rest_auth.registration.views import SocialLoginView


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client



@api_view(['POST'])
def usersignup(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)




@api_view(['GET'])
def usersignupdetail(request, pk):
    tasks = User.objects.get(id=pk)
    serializer = UserSerializer(tasks, many=False)
    return Response(serializer.data)




@api_view(['GET'])
def signuplist(request):
    tasks = User.objects.all()
    serializer = UserSerializer(tasks, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def userlist(request):
    tasks = Account.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def userdetail(request, pk):
    tasks = Account.objects.get(id=pk)
    serializer = TaskSerializer(tasks, many=False)
    return Response(serializer.data)



@api_view(['POST'])
def usercreate(request):
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def userupdate(request,pk):
    task = Account.objects.get(id=pk)
    serializer = TaskSerializer(instance = task ,data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)



@api_view(['DELETE'])
def userdelete(request,pk):
    task = Account.objects.get(id=pk)
    task.delete()
    return Response('Delete successfully.')








@api_view(['GET'])
def joblist(request):
    tasks = Job.objects.all()
    serializer = JobSerializer(tasks, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def jobdetail(request, pk):
    tasks = Job.objects.get(id=pk)
    serializer = JobSerializer(tasks, many=False)
    return Response(serializer.data)



@api_view(['POST'])
def jobcreate(request):
    serializer = JobSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def jobupdate(request,pk):
    task = Job.objects.get(id=pk)
    serializer = JobSerializer(instance = task ,data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)



@api_view(['DELETE'])
def jobdelete(request,pk):
    task = Job.objects.get(id=pk)
    task.delete()
    return Response('Delete successfully.')




@api_view(['GET'])
def orderlist(request):
    tasks = Order.objects.all()
    serializer = OrderSerializer(tasks, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def orderdetail(request, pk):
    tasks = Order.objects.get(id=pk)
    serializer = OrderSerializer(tasks, many=False)
    return Response(serializer.data)



@api_view(['POST'])
def checkout(request):
    serializer = OrderSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def orderdelete(request,pk):
    task = Order.objects.get(id=pk)
    task.delete()
    return Response('Delete successfully.')


def PaypalToken(client_ID, client_Secret):

    url = "https://api.sandbox.paypal.com/v1/oauth2/token"
    data = {
                "client_id":client_ID,
                "client_secret":client_Secret,
                "grant_type":"client_credentials"
            }
    headers = {
                "Content-Type": "application/x-www-form-urlencoded",
                "Authorization": "Basic {0}".format(base64.b64encode((client_id + ":" + client_secret).encode()).decode())
            }

    token = requests.post(url, data, headers=headers)
    return token


@api_view(['POST'])
def paypal(request):
    headers = {"Content-Type": "application/json", "Authorization": 'Bearer' +token}
    url = 'https://api.sandbox.paypal.com/v2/checkout/orders'

    data = {
                "intent": "CAPTURE",
                "application_context": {
                    "return_url": "https://www.example.com",
                    "cancel_url": "https://www.example.com",
                    "brand_name": "EXAMPLE INC",
                    "landing_page": "BILLING",
                    "shipping_preference": "SET_PROVIDED_ADDRESS",
                    "user_action": "CONTINUE"
                },
                "purchase_units": [
                    {
                        "reference_id": "PUHF",
                        "description": "Sporting Goods",

                        "custom_id": "CUST-HighFashions",
                        "soft_descriptor": "HighFashions",
                        "amount": {
                            "currency_code": "USD",
                            "value": "220.00",
                            "breakdown": {
                                "item_total": {
                                    "currency_code": "USD",
                                    "value": "180.00"
                                },
                                "shipping": {
                                    "currency_code": "USD",
                                    "value": "20.00"
                                },
                                "handling": {
                                    "currency_code": "USD",
                                    "value": "10.00"
                                },
                                "tax_total": {
                                    "currency_code": "USD",
                                    "value": "20.00"
                                },
                                "shipping_discount": {
                                    "currency_code": "USD",
                                    "value": "10"
                                }
                            }
                        },
                        "items": [
                            {
                                "name": "T-Shirt",
                                "description": "Green XL",
                                "sku": "sku01",
                                "unit_amount": {
                                    "currency_code": "USD",
                                    "value": "90.00"
                                },
                                "tax": {
                                    "currency_code": "USD",
                                    "value": "10.00"
                                },
                                "quantity": "1",
                                "category": "PHYSICAL_GOODS"
                            },
                            {
                                "name": "Shoes",
                                "description": "Running, Size 10.5",
                                "sku": "sku02",
                                "unit_amount": {
                                    "currency_code": "USD",
                                    "value": "45.00"
                                },
                                "tax": {
                                    "currency_code": "USD",
                                    "value": "5.00"
                                },
                                "quantity": "2",
                                "category": "PHYSICAL_GOODS"
                            }
                        ],
                        "shipping": {
                            "method": "United States Postal Service",
                            "name": {
                                "full_name":"John Doe"
                            },
                            "address": {
                                "address_line_1": "123 Townsend St",
                                "address_line_2": "Floor 6",
                                "admin_area_2": "San Francisco",
                                "admin_area_1": "CA",
                                "postal_code": "94107",
                                "country_code": "US"
                            }
                        }
                    }
                ]
            }
    result = requests.post(url, data, headers=header)
