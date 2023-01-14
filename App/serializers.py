from rest_framework import serializers
from App.models import Wallet, Users, Crypto, Transactions

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ('WalletId', 'WalletVault', 'WalletBTC', 'WalletETH', 'WalletUSDT', 'WalletBUSD', 'WalletSOL', 'WalletGALA',
                  'WalletXRP', 'WalletADA', 'WalletLTC', 'WalletDOGE', 'WalletBNB', 'WalletZIL', 'WalletMATIC', 'WalletAVAX') 

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('UserId', 'UserRole', 'UserName', 'UserSurname', 'UserEmail', 'UserProfileURL', 'UserFacebookURL', 
                  'UserInstagramURL', 'UserTwitterURL', 'UserPassword', 'UserStatus', 'UserWallet')

class CryptoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crypto
        fields = ('CryptoId', 'CryptoIcon', 'CryptoName', 'CryptoAbbreviation', 'CryptoCurrentPrice')

class TransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = ('TransactionId', 'TransactionActionType', 'TransactionCryptoType', 'TransactionAmount', 
                  'TransactionTime', 'TransactionsUser')
                  