from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework import status

from App.models import Wallet, Users, Crypto, Transactions
from App.serializers import WalletSerializer, UsersSerializer, CryptoSerializer, TransactionsSerializer

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
            return JsonResponse({'message': 'Record has been added successfully'}, status = status.HTTP_201_CREATED, safe = False) 
        else:
            return JsonResponse({'message': 'Failed to add new record'}, status = status.HTTP_400_BAD_REQUEST, safe = False)

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

        