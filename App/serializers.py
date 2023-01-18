from rest_framework import serializers
from App.models import Wallet, User, Crypto, Transactions

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('UserId', 'UserRole', 'UserFirstName', 'UserSurname', 'UserEmail', 'UserProfileURL', 'UserFacebookURL', 
                  'UserInstagramURL', 'UserTwitterURL', 'UserPassword', 'UserStatus')
        extra_kwargs = {
            'UserPassword': {'write_only': True}
        }

    def create(self, validated_data):
        UserPassword = validated_data.pop('UserPassword', None)
        UserInstance = self.Meta.model(**validated_data)

        if UserPassword is not None:
            UserInstance.set_password(UserPassword)
        UserInstance.save()
        return UserInstance


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ('WalletId', 'WalletVault', 'WalletBTC', 'WalletETH', 'WalletUSDT', 'WalletBUSD', 'WalletSOL', 'WalletGALA',
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
                  