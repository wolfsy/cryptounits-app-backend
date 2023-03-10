from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.authentication import get_authorization_header

from App.models import Wallet, User, Crypto, Transactions
from App.serializers import WalletSerializer, UserSerializer, CryptoSerializer, TransactionsSerializer
from App.backend import NewBackend
from App.authentication import create_access_token, decode_access_token

# Create your views here.

@api_view(['GET', 'POST', 'DELETE'])
def wallet_list(request):
    if request.method == 'GET':
        wallets = Wallet.objects.all()
        wallets_serializer = WalletSerializer(wallets, many = True)
        return JsonResponse(wallets_serializer.data, safe = False)

    elif request.method == 'POST':
        wallet_data = JSONParser().parse(request)
        wallet_serializer = WalletSerializer(data = wallet_data)
        if wallet_serializer.is_valid():
            wallet_serializer.save()
            return JsonResponse({'message': 'Record has been added successfully.'}, status = status.HTTP_201_CREATED, safe = False) 
        else:
            return JsonResponse({'message': 'Failed to add new record.'}, status = status.HTTP_400_BAD_REQUEST, safe = False)

    elif request.method == 'DELETE':
        wallets = Wallet.objects.all().delete()
        return JsonResponse({'message': '{} wallet records were deleted successfully!'.format(wallets[0])},
            status = status.HTTP_204_NO_CONTENT, safe = False)
 
@api_view(['GET' ,'PUT', 'DELETE'])
def wallet_detail(request, id):
    try:
        wallet = Wallet.objects.get(WalletId = id)
    except Wallet.DoesNotExist:
        return JsonResponse({'message': 'The wallet object does not exist!'}, status = status.HTTP_404_NOT_FOUND, safe = False)
        
    if request.method == 'GET':
        wallet_serializer = WalletSerializer(wallet)
        return JsonResponse(wallet_serializer.data)

    elif request.method == 'PUT':
        wallet_data = JSONParser().parse(request) 
        wallet_serializer = WalletSerializer(wallet, data = wallet_data) 
        if wallet_serializer.is_valid(): 
            wallet_serializer.save() 
            return JsonResponse({'message': 'The wallet object has been updated successfully!'}, safe = False) 
        else:
            return JsonResponse(wallet_serializer.errors, status = status.HTTP_400_BAD_REQUEST, safe = False) 

    elif request.method == 'DELETE':
        wallet.delete()
        return JsonResponse({'message': 'The wallet object has been deleted successfully!'}, status = status.HTTP_204_NO_CONTENT, safe = False)

@api_view(['GET'])
def crypto_list(request):
    if request.method == 'GET':
        cryptos = Crypto.objects.filter().order_by('CryptoCurrentPrice')
        cryptos_serializer = CryptoSerializer(cryptos, many = True)
        return JsonResponse(cryptos_serializer.data, safe = False)

@api_view(['POST'])
def register_user(request):
    users_serializer = UserSerializer(data = request.data)
    user = User.objects.filter(UserEmail = request.data['UserEmail']).first()

    if user:
        return JsonResponse({'message': 'Passed address e-mail is already registered!'}, status = status.HTTP_409_CONFLICT, safe = False)

    if users_serializer.is_valid():
        users_serializer.save()
        return JsonResponse(users_serializer.data, safe = False) 
    else:
        return JsonResponse({'message': 'Failed to register new user.'}, status = status.HTTP_400_BAD_REQUEST, safe = False)

@api_view(['POST'])
def login_user(request):
    user = User.objects.filter(UserEmail = request.data['UserEmail']).first()
    users_serializer = UserSerializer(data = request.data)

    if users_serializer.is_valid():
        NewBackend.authenticate(request, user)

        accessToken = create_access_token(user.UserId)
        response = Response()
        response.set_cookie(key = 'JWT', value = accessToken, httponly = True)

        response.data = {
            'JWT': accessToken
        }  

        return response
    return JsonResponse({'message': 'Users serializer is invalid!'})

@api_view(['GET'])
def user_view(request):
    auth = get_authorization_header(request).split()

    if auth and len(auth) == 2:
        accessToken = auth[1].decode('utf-8')
        UserId = decode_access_token(accessToken)
        user = User.objects.filter(UserId = UserId).first()
        users_serializer = UserSerializer(user)
        return JsonResponse(users_serializer.data) 

    if not accessToken:
        raise AuthenticationFailed('User unauthenticated!')

@api_view(['POST'])
def logout_user(response):
    response = Response()
    response.delete_cookie('JWT')
    response.data = {
        'message': 'User has successfully logout.'
    }
    return response

@api_view(['GET'])
def user_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        users_serializer = UserSerializer(users, many = True)
        return JsonResponse(users_serializer.data, safe = False)

@api_view(['POST'])
def perform_transaction(request):
    transaction_data = JSONParser().parse(request)
    transaction_serializer = TransactionsSerializer(data = transaction_data)
    if transaction_serializer.is_valid():
        transaction_serializer.save()
        return JsonResponse({'message': 'Record has been added successfully.'}, status = status.HTTP_201_CREATED, safe = False) 
    else:
        return JsonResponse({'message': 'Failed to add new record.'}, status = status.HTTP_400_BAD_REQUEST, safe = False)