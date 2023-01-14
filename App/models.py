from django.db import models

# Create your models here.
class Wallet(models.Model):
    WalletId = models.AutoField(primary_key = True)
    WalletVault = models.FloatField()
    WalletBTC = models.FloatField()
    WalletETH = models.FloatField()
    WalletUSDT = models.FloatField()
    WalletBUSD = models.FloatField()
    WalletSOL = models.FloatField()
    WalletGALA = models.FloatField()
    WalletXRP = models.FloatField()
    WalletADA = models.FloatField()
    WalletLTC = models.FloatField()
    WalletDOGE = models.FloatField()
    WalletBNB = models.FloatField()
    WalletZIL = models.FloatField()
    WalletMATIC = models.FloatField()
    WalletAVAX = models.FloatField()

class Users(models.Model):
    UserId = models.AutoField(primary_key = True)
    UserRole = models.CharField(max_length = 100)
    UserName = models.CharField(max_length = 100)
    UserSurname = models.CharField(max_length = 100)
    UserEmail = models.CharField(max_length = 100)
    UserProfileURL = models.CharField(max_length = 255)
    UserFacebookURL = models.CharField(max_length = 255)
    UserInstagramURL = models.CharField(max_length = 255)
    UserTwitterURL = models.CharField(max_length = 255)
    UserPassword = models.CharField(max_length = 255)
    UserStatus = models.BooleanField
    UserWallet = models.ForeignKey(Wallet, on_delete = models.CASCADE) 

class Crypto(models.Model):
    CryptoId = models.AutoField(primary_key = True)
    CryptoIcon = models.CharField(max_length = 100)
    CryptoName = models.CharField(max_length = 100)
    CryptoAbbreviation = models.CharField(max_length = 100)
    CryptoCurrentPrice = models.FloatField()

class Transactions(models.Model):
    TransactionId = models.AutoField(primary_key = True)
    TransactionActionType = models.CharField(max_length = 100)
    TransactionCryptoType = models.CharField(max_length = 100)
    TransactionAmount = models.FloatField()
    TransactionTime = models.DateTimeField(auto_now_add = True) 
    TransactionsUser = models.ForeignKey(Users, on_delete = models.CASCADE)