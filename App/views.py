from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from App.models import Wallet, Users, Crypto, Transactions
from App.serializers import WalletSerializer, UsersSerializer, CryptoSerializer, TransactionsSerializer

# Create your views here.
