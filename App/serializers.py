from rest_framework import serializers
from App.models import Wallet, User, Crypto, Transactions
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('UserId', 'UserFirstName', 'UserSurname', 'UserEmail', 'UserProfileURL', 'UserPassword')
        extra_kwargs = {
            'UserPassword': {'write_only': True}, 'UserFirstName': {'required': False}, 'UserSurname': {'required': False},
            'UserEmail': {'validators': []}
        }

    def create(self, validated_data):
        validated_data['UserPassword'] = make_password(validated_data['UserPassword'], None)
        return super(UserSerializer, self).create(validated_data)

    # zmien z powrotem na glownego usera, usun na dole settings app.user i skonfiguruj normalnie 
    # user = User.objects.create_user(UserFirstName = 'UserFirstName', UserSurname = 'UserSurname',
    #     UserEmail = 'UserEmail', UserProfileURL = 'UserProfileURL', UserPassword = 'UserPassword', UserStatus = 'UserStatus')

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ('WalletId', 'WalletCard', 'WalletVault', 'WalletBTC', 'WalletETH', 'WalletUSDT', 'WalletBUSD', 'WalletSOL', 'WalletGALA',
                  'WalletXRP', 'WalletADA', 'WalletLTC', 'WalletDOGE', 'WalletBNB', 'WalletZIL', 'WalletMATIC', 'WalletAVAX', 'WalletUser') 

class CryptoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crypto
        fields = ('CryptoId', 'CryptoIcon', 'CryptoName', 'CryptoAbbreviation', 'CryptoCurrentPrice')

class TransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = ('TransactionId', 'TransactionActionType', 'TransactionCryptoType', 'TransactionAmount', 
                  'TransactionTime', 'TransactionsUser')
                  