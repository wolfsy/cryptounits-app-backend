from django.test import TestCase
from .models import User, Wallet, Crypto, Transactions

# Transaction test cases

class TransactionsModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            UserEmail = 'test@transaction.com', 
            UserPassword = 'test'
        )
        self.transaction = Transactions.objects.create(
            TransactionActionType = 'deposit',
            TransactionCryptoType = 'BTC',
            TransactionAmount = 0.1,
            TransactionsUser = self.user
        )

    def tearDown(self):
        self.transaction.delete()
        self.user.delete()

    def test_transaction_creation(self):
        self.assertTrue(Transactions.objects.exists())
        self.assertEqual(Transactions.objects.count(), 1)
        print(f"\nNewly transaction number {self.transaction.TransactionId} created:", self.transaction.TransactionActionType, self.transaction.TransactionCryptoType,
              self.transaction.TransactionAmount, self.transaction.TransactionsUser)
        
    def test_transaction_details(self):
        transaction = Transactions.objects.get(TransactionId = self.transaction.TransactionId)
        self.assertEqual(transaction.TransactionActionType, 'deposit')
        self.assertEqual(transaction.TransactionCryptoType, 'BTC')
        self.assertEqual(transaction.TransactionAmount, 0.1)
        self.assertEqual(transaction.TransactionsUser, self.user)
        print("\nThe transaction has proper values of passed arguments.")

# Wallet test cases

class WalletModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            UserEmail = 'test@wallet.com', 
            UserPassword = 'test'
        )
        self.wallet = Wallet.objects.create(
            WalletAddress = '1b0120x6789abdsef01232189abcdef0123',
            WalletCard = '1111222233334444',
            WalletBTC = 0.0,
            WalletUser = self.user
        )

    def tearDown(self):
        self.user.delete()
        self.wallet.delete()

    def test_wallet_address_max_length(self):
        wallet = Wallet.objects.get(WalletAddress = self.wallet.WalletAddress)
        max_length = wallet._meta.get_field('WalletAddress').max_length
        self.assertEquals(max_length, 35)
        print("\nThe wallet address value has the proper length.")

    def test_wallet_vault_default_value(self):
        wallet = Wallet.objects.get(WalletVault = self.wallet.WalletVault)
        self.assertEquals(wallet.WalletVault, 0.0)
        print("\nThe default value of the wallet status has been set correctly.")

    def test_wallet_user_relation(self):
        wallet = Wallet.objects.get(WalletId = self.wallet.WalletId)
        self.assertEquals(wallet.WalletUser.UserEmail, 'test@wallet.com')
        print(f"\nWallets relation of the e-mail: {wallet.WalletUser.UserEmail} was equal to the passed argument.")

# Crypto test cases

class CryptoModelTestCase(TestCase):
    def setUp(self):
        self.crypto = Crypto.objects.create(
            CryptoIcon = 'https://cryptologos.cc/logos/bitcoin-btc-logo.svg?v=024',
            CryptoName = 'Bitcoin',
            CryptoAbbreviation = 'BTC',
            CryptoCurrentPrice = 100000.00
        )

    def tearDown(self):
        self.crypto.delete()

    def test_crypto_icon_max_length(self):
        crypto = Crypto.objects.get(CryptoIcon = self.crypto.CryptoIcon)
        max_length = crypto._meta.get_field('CryptoIcon').max_length
        self.assertEquals(max_length, 100)
        print("\nThe passed argument has the proper length.")

    def test_crypto_name(self):
        crypto = Crypto.objects.get(CryptoName = self.crypto.CryptoName)
        self.assertEquals(crypto.CryptoName, 'Bitcoin')
        print("\nThe passed pattern was equal to the value in the created test object.")

    def test_crypto_abbreviation(self):
        crypto = Crypto.objects.get(CryptoAbbreviation = self.crypto.CryptoAbbreviation)
        self.assertEquals(crypto.CryptoAbbreviation, 'BTC')
        print("\nThe passed crypto abbreviation was equal.")
