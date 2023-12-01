from django.db import models

from heroku_tb_backend import settings

class Merchant(models.Model):
    merchantId = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    payment_method = models.CharField(max_length=255)
    box_premium = models.IntegerField(default=0)
    box_common = models.IntegerField(default=0)

    def get_merchant_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.get_merchant_full_name()

class MerchantTransaction(models.Model):
    BOXTYPES = (
        ("premium", "Premium"),
        ("common", "Common"),
    )

    TRANSACTIONTYPES = (
        ("lend", "Lend"),
        ("devolution", "Devolution"),
    )


    merchantTransactionId = models.AutoField(primary_key=True)
    merchant = models.ForeignKey(to=Merchant, related_name='transactions', on_delete=models.CASCADE)
    merchant_name = models.CharField(max_length=200, blank=True, null=True) 
    date = models.DateField(auto_now_add=True)  
    transaction_type = models.CharField(max_length=15, choices=TRANSACTIONTYPES)
    box_type = models.CharField(max_length=10, choices=BOXTYPES)
    box_qtt = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        if self.merchant:
            self.merchant_name = self.merchant.get_merchant_full_name()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.merchant_name
