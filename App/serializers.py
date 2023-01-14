from rest_framework import serializers
from App.models import Wallet, Users, Crypto, Transactions

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ('WalletId', 'WalletVault', 'WalletBTC', 'WalletETH', 'WalletUSDT', 'WalletBUSD', 'WalletSOL', 'WalletGALA',
                  'WalletXRP', 'WalletADA', 'WalletLTC', 'WalletDOGE', 'WalletBNB', 'WalletZIL', 'WalletMATIC', 'WalletAVAX') 

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('UserId', 'UserRole', 'UserName', 'UserSurname', 'UserEmail', 'UserProfileURL', 'UserFacebookURL', 
                  'UserInstagramURL', 'UserTwitterURL', 'UserPassword', 'UserStatus', 'UserWallet')

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crypto
        fields = ('CryptoId', 'CryptoIcon', 'CryptoName', 'CryptoAbbreviation', 'CryptoCurrentPrice')

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = ('TransactionId', 'TransactionActionType', 'TransactionCryptoType', 'TransactionAmount', 
                  'TransactionTime', 'TransactionsUser')