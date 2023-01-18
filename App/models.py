from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    UserId = models.AutoField(primary_key = True)
    UserRole = models.CharField(max_length = 100, default = "USER")
    UserFirstName = models.CharField(max_length = 100)
    UserSurname = models.CharField(max_length = 100)
    UserEmail = models.CharField(max_length = 100, unique = True)
    UserProfileURL = models.CharField(max_length = 255, blank = True, null = True)
    UserFacebookURL = models.CharField(max_length = 255, blank = True, null = True)
    UserInstagramURL = models.CharField(max_length = 255, blank = True, null = True)
    UserTwitterURL = models.CharField(max_length = 255, blank = True, null = True)
    UserPassword = models.CharField(max_length = 255)
    UserStatus = models.BooleanField(default = True)

    username = None
    USERNAME_FIELD = 'UserEmail'
    REQUIRED_FIELDS = []

class Wallet(models.Model):
    WalletId = models.AutoField(primary_key = True)
    WalletVault = models.FloatField(default = 0.0)
    WalletBTC = models.FloatField(default = 0.0)
    WalletETH = models.FloatField(default = 0.0)
    WalletUSDT = models.FloatField(default = 0.0)
    WalletBUSD = models.FloatField(default = 0.0)
    WalletSOL = models.FloatField(default = 0.0)
    WalletGALA = models.FloatField(default = 0.0)
    WalletXRP = models.FloatField(default = 0.0)
    WalletADA = models.FloatField(default = 0.0)
    WalletLTC = models.FloatField(default = 0.0)
    WalletDOGE = models.FloatField(default = 0.0)
    WalletBNB = models.FloatField(default = 0.0)
    WalletZIL = models.FloatField(default = 0.0)
    WalletMATIC = models.FloatField(default = 0.0)
    WalletAVAX = models.FloatField(default = 0.0)
    WalletUser = models.ForeignKey(User, on_delete = models.CASCADE) 

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
    TransactionsUser = models.ForeignKey(User, on_delete = models.CASCADE)